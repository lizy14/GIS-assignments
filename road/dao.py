import shapefile
from config import *

_sf = shapefile.Reader(FILENAME)

print ("Loading shapes from `{}` ...".format(FILENAME))
shapes = _sf.shapes()

assert(len(shapes) > 0)
print ("Loaded {} shapes. ".format(len(shapes)))

__all__ = ['shapes']
