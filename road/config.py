from os import path

DEBUG = 1

QGIS_PATH = 'C:\\Program Files\\QGIS Las\\apps\\qgis'

FILENAME = path.abspath(path.join(
    path.dirname(__file__),
    path.pardir,
    'data',
    'soil.shp'
))
# alternatively,
# FILENAME = 'C:\\_O\\GIS-assignments\\data\\road.shp'
