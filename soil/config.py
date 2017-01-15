from os import path

DEBUG = 1
FILENAME = path.abspath(path.join(
    path.dirname(__file__),
    path.pardir,
    'data',
    'soil.shp'
))
# alternatively,
# FILENAME = 'C:\\_O\\GIS-assignments\\data\\soil.shp'
