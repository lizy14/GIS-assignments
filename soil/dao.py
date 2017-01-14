import shapefile
from config import *

sf = shapefile.Reader(FILENAME)

print ("Loading shapes from `{}` ...".format(FILENAME))
shapes = sf.shapes()

assert(len(shapes) > 0)
print ("Loaded {} shapes. ".format(len(shapes)))

print (len(shapes[0].points))
print (shapes[0].bbox)
