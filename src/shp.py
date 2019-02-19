import shapefile as shp
import matplotlib.pyplot as plt

ZIPCODE = 'ZCTA5CE10'

print ('Reading shapefile...')
sf = shp.Reader('./data/usa-census-zipcodes/cb_2017_us_zcta510_500k')

shapes = sf.shapeRecords()
records = sf.records()

index = 1
shape = shapes[index]
record = records[index]

zipcode = record[ZIPCODE]
print('Zipcode:', zipcode)

print('Drawing...')
plt.figure()
x = [i[0] for i in shape.shape.points[:]]
y = [i[1] for i in shape.shape.points[:]]
plt.plot(x,y)
plt.show()