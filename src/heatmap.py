import json
import shapefile as shp
import matplotlib.pyplot as plt
from time import time
from PIL import Image
from colour import Color
from os import path, remove
from descartes import PolygonPatch

PATH = path.dirname(path.dirname(path.abspath(__file__)))

COUNTY_SHAPE_FILE = PATH +'/data/us-census/us-county-shapefiles-2017/cb_2017_us_county_500k'
ZIPCODE_SHAPE_FILE = PATH + '/data/us-census/us-zipcode-shapefiles-2017/cb_2017_us_zcta510_500k'
STATE_SHAPE_FILE = PATH + '/data/us-census/us-state-shapefiles-2017/cb_2017_us_state_500k'

COUNTY_SCORE_FILE = PATH + '/data/geo-scores/all-county-scores.json'
ZIPCODE_SCORE_FILE = PATH + '/data/geo-scores/all-zipcode-scores.json'
PNG_FILE = PATH + '/heatmaps/heatmap.png'
JPG_FILE = PATH + '/heatmaps/heatmap.jpg'

COUNTY_KEY = 'COUNTYNS'
ZIPCODE_KEY = 'GEOID10'

HIGH_COLOR = '#FF0909'
LOW_COLOR = '#4949E4'
BACKGROUND_COLOR = '#000000'
OUTLINE_COLOR = '#333333'
GRADIENT = list(Color(LOW_COLOR).range_to(Color(HIGH_COLOR), 1001))

LAT_BOUNDS = (24, 50) 
LONG_BOUNDS = (-126, -66)
IMG_SIZE = 50
IMG_RATIO = (LAT_BOUNDS[0] - LAT_BOUNDS[1]) / (LONG_BOUNDS[0] - LONG_BOUNDS[1]) / 0.77
IMG_DIMENSIONS = (IMG_SIZE, IMG_RATIO * IMG_SIZE)

def draw_shapes(shapefile, axes, id_key, scores, is_filled, is_outlined, zorder):
    shapes = shapefile.shapes()
    records = shapefile.records()

    for i in range(len(shapes)):
        polygon = shapes[i].__geo_interface__
        id = records[i][id_key]
        if id not in scores:
            fill_color = 'none'
        else:
            score = scores[id]
            fill_color = GRADIENT[score].hex_l
        edge_color = OUTLINE_COLOR if is_outlined else fill_color

        patch = PolygonPatch(polygon, fc=fill_color, ec=edge_color, alpha=1, zorder=zorder)
        axes.add_patch(patch)

if __name__ == '__main__':

    start = time()

    county_scores = json.load(open(COUNTY_SCORE_FILE))
    zipcode_scores = json.load(open(ZIPCODE_SCORE_FILE))

    county_shape_file = shp.Reader(COUNTY_SHAPE_FILE)
    zipcode_shape_file = shp.Reader(ZIPCODE_SHAPE_FILE)
    state_shape_file = shp.Reader(STATE_SHAPE_FILE)

    axes = plt.figure(figsize=IMG_DIMENSIONS).gca()
    axes.set_facecolor(BACKGROUND_COLOR)
    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    print('Drawing counties...')
    draw_shapes(county_shape_file, axes, COUNTY_KEY, county_scores, True, False, 1)
    print('Drawing zipcodes...')
    draw_shapes(zipcode_shape_file, axes, ZIPCODE_KEY, zipcode_scores, True, False, 2)
    print('Drawing states...')
    draw_shapes(state_shape_file, axes, False, {}, False, True, 3)

    print('Saving heatmap...')
    plt.xlim(LONG_BOUNDS)
    plt.ylim(LAT_BOUNDS)
    plt.savefig(PNG_FILE, bbox_inches='tight', pad_inches=0)
    Image.open(PNG_FILE).convert('RGB').save(JPG_FILE, 'JPEG')

    duration = round(time() - start, 2)
    print('Saved heatmap to', JPG_FILE, 'in', duration, 'seconds.')

    remove(PNG_FILE)
    Image.open(JPG_FILE).show()
    
