import json
import codecs

CLIMBING_AREAS_FILE = './data/climbing-areas-2019.json'
COUNTIES_FILE = './data/usa-counties-lat-long-2017.txt'
SCORES_FILE = './data/county-scores-raw.json'

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
    with codecs.open(COUNTIES_FILE, 'r', encoding='utf-8', errors='ignore') as file:
        rows = file.readlines()

    for row in rows[1:]:
        values = row.split()
        county = values[2]
        lat = values[8]
        long = values[9]
        score = calculate_score(float(lat), float(long), data, 0, 0)
        scores[county] = score

    with open(SCORES_FILE, 'w') as file:  
        json.dump(scores, file)
