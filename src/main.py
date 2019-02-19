import json
import matplotlib.pyplot as plt
from util import extract_routes, extract_areas

ORIGIN_X = -99.222991
ORIGIN_Y = 38.926142

with open('./data/data.json') as file:
  data = json.load(file)


areas = extract_areas(data)

plot_data_x = []
plot_data_y = []
for area in areas:
  if 'lat' in area and 'long' in area:
    plot_data_x.append(area['long'] - ORIGIN_X)
    plot_data_y.append(area['lat'] - ORIGIN_Y)

print(len(plot_data_x))

plt.scatter(plot_data_x, plot_data_y, marker='o')
plt.show()