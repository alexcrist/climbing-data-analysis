import shapefile as shp
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from colour import Color

ZIPCODE_KEY = 'ZCTA5CE10'
HIGH_COLOR = '#00ff00'
LOW_COLOR = '#333333'
OUTLINE_COLOR = '#000000'

zipcode_scores = { 98112: 40 }

print ('Reading shapefile...')
sf = shp.Reader('./data/usa-census-zipcodes/cb_2017_us_zcta510_500k')
shapes = sf.shapes()
records = sf.records()

colors = list(Color(LOW_COLOR).range_to(Color(HIGH_COLOR), 100))

axes = plt.figure().gca()

for i in range(len(shapes)):

    zipcode = records[i][ZIPCODE_KEY]
    polygon = shapes[i].__geo_interface__

    score = zipcode_scores[zipcode]
    color = colors[score]

    print('zipcode', zipcode)

    patch = PolygonPatch(polygon, fc=color, ec=OUTLINE_COLOR, alpha=0.5, zorder=2)
    axes.add_patch(patch)

ax.axis('scaled')
plt.show()