import shapefile

from config import *
import logging
logging.basicConfig(level=1)
_logger = logging.getLogger(__name__)

_sf = shapefile.Reader(FILENAME)

_logger.info("Loading shapes from `{}` ...".format(FILENAME))
shapes = _sf.shapes()

assert(len(shapes) > 0)
_logger.info("Loaded {} shapes. ".format(len(shapes)))

__all__ = ['shapes']
