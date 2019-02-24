import json
import codecs
import operator
import numpy as np
from math import exp
from time import time

CLIMBING_AREAS_FILE = './data/flattened-climbing-routes-2019.json'
COUNTIES_FILE = './data/usa-counties-lat-long-2017.txt'
SCORES_FILE = './data/county-scores.json'

NUM_CLIMBING_FIELDS = 4
AVG_RATING = 0
NUM_RATINGS = 1
ROUTE_LAT = 2
ROUTE_LONG = 3

def load_climbing_data():
    climbing_data = []
    raw_climbing_data = json.load(open(CLIMBING_AREAS_FILE))

    for row in raw_climbing_data:
        entry = [0] * NUM_CLIMBING_FIELDS
        entry[AVG_RATING] = row['avgRating']
        entry[NUM_RATINGS] = row['numRatings']
        entry[ROUTE_LAT] = row['lat']
        entry[ROUTE_LONG] = row['long']
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

def calculate_score(lat, long, climbing_data):
    dLat = climbing_data[:,ROUTE_LAT] - lat 
    dLong = climbing_data[:,ROUTE_LONG] - long

    dLatSquared = np.multiply(dLat, dLat)
    dLongSquared = np.multiply(dLong, dLong)

    distance = np.sqrt(dLatSquared + dLongSquared)
    distanceScore = np.exp(np.multiply(-1, distance))

    ratingScore = np.multiply(climbing_data[:,AVG_RATING], climbing_data[:,NUM_RATINGS])
    score = np.multiply(ratingScore, distanceScore)

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

if __name__ == '__main__':

    start = time()

    climbing_data = load_climbing_data()
    county_data = load_county_data()

    scores = {}
    for county in county_data:
        score = calculate_score(county['lat'], county['long'], climbing_data)
        scores[county['id']] = score

    normalized_scores = normalize_scores(scores)

    with open(SCORES_FILE, 'w') as file:  
        json.dump(normalized_scores, file)

    duration = round(time() - start, 2)
    print('Scored US counties to', SCORES_FILE, 'in', duration, 'seconds.')
