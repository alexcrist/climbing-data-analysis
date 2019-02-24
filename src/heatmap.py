import json
import shapefile as shp
import matplotlib.pyplot as plt
from time import time
from PIL import Image
from colour import Color
from descartes import PolygonPatch

SHAPE_FILE = './data/usa-counties-shapefiles-2017/cb_2017_us_county_500k'
SCORE_FILE = './data/county-scores.json'
PNG_FILE = './heatmap.png'
JPG_FILE = './heatmap.jpg'

COUNTY_KEY = 'COUNTYNS'

HIGH_COLOR = '#FF0909'
LOW_COLOR = '#4949E4'
BACKGROUND_COLOR = '#EEEEEE'

LAT_BOUNDS = (25, 50) 
LONG_BOUNDS = (-126, -66)
IMG_SIZE = 50
IMG_RATIO = (LAT_BOUNDS[0] - LAT_BOUNDS[1]) / (LONG_BOUNDS[0] - LONG_BOUNDS[1]) / 0.77
IMG_DIMENSIONS = (IMG_SIZE, IMG_RATIO * IMG_SIZE)

if __name__ == '__main__':

    start = time()

    with open(SCORE_FILE) as file:
        scores = json.load(file)

    shapefile = shp.Reader(SHAPE_FILE)
    shapes = shapefile.shapes()
    records = shapefile.records()

    gradient = list(Color(LOW_COLOR).range_to(Color(HIGH_COLOR), 1001))
    axes = plt.figure(figsize=IMG_DIMENSIONS).gca()
    axes.set_facecolor(BACKGROUND_COLOR)
    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    for i in range(len(shapes)):
        polygon = shapes[i].__geo_interface__
        county = records[i][COUNTY_KEY]
        
        if county not in scores:
            continue

        score = scores[county]
        color = gradient[score].hex_l

        patch = PolygonPatch(polygon, fc=color, ec='none', alpha=1, zorder=2)
        axes.add_patch(patch)

    plt.xlim(LONG_BOUNDS)
    plt.ylim(LAT_BOUNDS)
    plt.savefig(PNG_FILE, bbox_inches='tight', transparent=True, pad_inches=0)
    Image.open(PNG_FILE).convert('RGB').save(JPG_FILE, 'JPEG')

    duration = round(time() - start, 2)
    print('Saved heatmap to', JPG_FILE, 'in', duration, 'seconds.')

    Image.open(JPG_FILE).show()
    
