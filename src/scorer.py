import csv
import json

CLIMBING_AREAS_FILE = './data/climbing-areas.json'
ZIPCODE_FILE = './data/zipcode-lat-long.txt'
SCORES_FILE = './data/scores.json'

def calculate_score(lat, long, node, node_lat, node_long):
    node_is_list = isinstance(node, list)
    node_is_area = 'children' in node

    if node_is_list:
        score = 0
        for sub_node in node:
            score += calculate_score(lat, long, sub_node, node_lat, node_long)
        return score

    elif node_is_area:
        if 'lat' in node and 'long' in node:
            node_lat = node['lat']
            node_long = node['long']
        return calculate_score(lat, long, node['children'], node_lat, node_long)

    else:
        distance = ((lat - node_lat)**2 + (long - node_long)**2)**0.5
        avg_rating = node['avgRating']
        num_ratings = node['numRatings']
        score = (avg_rating**2 * num_ratings) / (2 * distance)
        return score

if __name__ == '__main__':

    with open(CLIMBING_AREAS_FILE) as file:
        data = json.load(file)

    scores = {}
    with open(ZIPCODE_FILE) as file:
        reader = csv.reader(file)
        for [zipcode, lat, long] in reader:
            score = calculate_score(float(lat), float(long), data, 0, 0)
            scores[zipcode] = score
            print('.', end='', flush=True)

    with open(SCORES_FILE, 'w') as file:  
        json.dump(scores, file)
