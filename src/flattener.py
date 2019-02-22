import json

CLIMBING_AREAS_FILE = './data/climbing-areas-2019.json'
FLATTENED_FILE = './data/flattened-climbing-routes-2019.json'

def flatten_data(node, node_lat, node_long):
    node_is_list = isinstance(node, list)
    node_is_area = 'children' in node

    if node_is_list:
        flattened_data = []
        for sub_node in node:
            flattened_data += flatten_data(sub_node, node_lat, node_long)
        return flattened_data

    elif node_is_area:
        if 'lat' in node and 'long' in node:
            node_lat = node['lat']
            node_long = node['long']
        return flatten_data(node['children'], node_lat, node_long)

    else:
        node['lat'] = node_lat
        node['long'] = node_long
        return [node]

if __name__ == '__main__':

    with open(CLIMBING_AREAS_FILE) as file:
        data = json.load(file)

    flattened_data = flatten_data(data, 0, 0)

    with open(FLATTENED_FILE, 'w') as file:
        json.dump(flattened_data, file)
