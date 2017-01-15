from os import path

DEBUG = 1

QGIS_PATH = 'C:\\Program Files\\QGIS Las\\apps\\qgis'

FILENAME = path.abspath(path.join(
    path.dirname(__file__),
    path.pardir,
    'data',
    'road.shp'
))
# alternatively,
# FILENAME = 'C:\\_O\\GIS-assignments\\data\\road.shp'

__all__ = ['DEBUG', 'QGIS_PATH', 'FILENAME']
