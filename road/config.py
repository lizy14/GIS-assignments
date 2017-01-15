from os import path

DEBUG = 1
FILENAME = path.abspath(path.join(
    path.dirname(__file__),
    path.pardir,
    'data',
    'road.shp'
))
# alternatively,
# FILENAME = 'C:\\_O\\GIS-assignments\\data\\road.shp'
