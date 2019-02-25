import json
import codecs
import operator
import numpy as np
from math import exp, isnan
from time import time

CLIMBING_AREAS_FILE = './data/rock-climbing/flattened-climbing-routes-2019.json'
COUNTIES_FILE = './data/us-census/us-county-lat-long-2017.txt'
ZIPCODES_FILE = './data/us-census/us-zipcode-lat-long-2017.txt'
COUNTY_SCORES_FILE = './data/geo-scores/county-scores.json'
ZIPCODE_SCORES_FILE = './data/geo-scores/zipcode-scores.json'

NUM_CLIMBING_FIELDS = 13
AVG_RATING = 0
NUM_RATINGS = 1
ROUTE_LAT = 2
ROUTE_LONG = 3
ROUTE_IS_TRAD = 4
ROUTE_IS_SPORT = 5
ROUTE_IS_BOULDER = 6
ROUTE_IS_ALPINE = 7
ROUTE_IS_MIXED = 8
ROUTE_IS_ICE = 9
ROUTE_IS_SNOW = 10
ROUTE_IS_AID = 11
ROUTE_IS_TOPROPE = 12

LAT_BOUNDS = (24, 50) 
LONG_BOUNDS = (-126, -66)

def load_climbing_data():
    climbing_data = []
    raw_climbing_data = json.load(open(CLIMBING_AREAS_FILE))

    for row in raw_climbing_data:
        entry = [0] * NUM_CLIMBING_FIELDS
        entry[AVG_RATING] = row['avgRating']
        entry[NUM_RATINGS] = row['numRatings']
        entry[ROUTE_LAT] = row['lat']
        entry[ROUTE_LONG] = row['long']
        entry[ROUTE_IS_TRAD] = 1 if 'types' in row and 'trad' in row['types'] else 0
        entry[ROUTE_IS_SPORT] = 1 if 'types' in row and 'sport' in row['types'] else 0
        entry[ROUTE_IS_BOULDER] = 1 if 'types' in row and 'boulder' in row['types'] else 0
        entry[ROUTE_IS_ALPINE] = 1 if 'types' in row and 'alpine' in row['types'] else 0
        entry[ROUTE_IS_MIXED] = 1 if 'types' in row and 'mixed' in row['types'] else 0
        entry[ROUTE_IS_ICE] = 1 if 'types' in row and 'ice' in row['types'] else 0
        entry[ROUTE_IS_SNOW] = 1 if 'types' in row and 'snow' in row['types'] else 0
        entry[ROUTE_IS_AID] = 1 if 'types' in row and 'aid' in row['types'] else 0
        entry[ROUTE_IS_TOPROPE] = 1 if 'types' in row and 'tr' in row['types'] else 0
        climbing_data.append(entry)

    return np.array(climbing_data)

def load_county_data():
    raw_county_data = codecs.open(COUNTIES_FILE, 'r', encoding='utf-8', errors='ignore')
    raw_county_data = raw_county_data.readlines()[1:]
    county_data = []

    for row in raw_county_data:
        values = row.split('\t')
        county = {}
        county['id'] = values[2]
        county['lat'] = float(values[8])
        county['long'] = float(values[9])
        county_data.append(county)

    return county_data

def load_zipcode_data():
    raw_zipcode_data = codecs.open(ZIPCODES_FILE, 'r', encoding='utf-8', errors='ignore')
    raw_zipcode_data = raw_zipcode_data.readlines()[1:]
    zipcode_data = []

    for row in raw_zipcode_data:
        values = row.split(',')
        zipcode = {}
        zipcode['id'] = values[0]
        zipcode['lat'] = float(values[1])
        zipcode['long'] = float(values[2])
        zipcode_data.append(zipcode)

    return zipcode_data

def calculate_score(lat, long, climbing_data):
    dLat = climbing_data[:,ROUTE_LAT] - lat 
    dLong = climbing_data[:,ROUTE_LONG] - long

    dLatSquared = np.multiply(dLat, dLat)
    dLongSquared = np.multiply(dLong, dLong)

    distance = np.sqrt(dLatSquared + dLongSquared)
    distanceScore = np.exp(np.multiply(-1, distance))

    ratingScore = np.multiply(climbing_data[:,AVG_RATING], climbing_data[:,NUM_RATINGS])
    score = np.multiply(ratingScore, distanceScore)

    # Filters routes by type
    # score = np.multiply(score, climbing_data[:,ROUTE_IS_TRAD])

    return np.log(np.sum(score) + 1)

def normalize_scores(scores):
    min_score = 99999999
    max_score = 0
    for county, score in scores.items():
        max_score = max(score, max_score)
        min_score = min(score, min_score)

    normalized_scores = {}
    for county, score in scores.items():
        normalized_score = int(round((score - min_score) / (max_score - min_score) * 1000))

        normalized_score = int(round(score / max_score * 1000))
        normalized_scores[county] = normalized_score

    return normalized_scores

def score_data(climbing_data, geo_data, scores_file):
    start = time()
    scores = {}
    for geo in geo_data:
        lat_inbounds = LAT_BOUNDS[0] < geo['lat'] < LAT_BOUNDS[1]
        long_inbounds = LONG_BOUNDS[0] < geo['long'] < LONG_BOUNDS[1]
        if lat_inbounds and long_inbounds:
            score = calculate_score(geo['lat'], geo['long'], climbing_data)
            scores[geo['id']] = score

    normalized_scores = normalize_scores(scores)

    with open(scores_file, 'w') as file:  
        json.dump(normalized_scores, file)

    duration = round(time() - start, 2)
    print('Created scores in', scores_file, 'in', duration, 'seconds.')

if __name__ == '__main__':

    climbing_data = load_climbing_data()
    county_data = load_county_data()
    zipcode_data = load_zipcode_data()

    print('Scoring counties...')
    score_data(climbing_data, county_data, COUNTY_SCORES_FILE)

    print('Scoring zipcodes...')
    score_data(climbing_data, zipcode_data, ZIPCODE_SCORES_FILE)
