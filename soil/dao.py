import shapefile
import logging
from config import DEBUG
from config import FILENAME
logging.basicConfig(level=DEBUG)
_logger = logging.getLogger(__name__)


def load_shapes(filename):
    _sf = shapefile.Reader(filename)

    _logger.info("Loading shapes from `{}` ...".format(filename))
    shapes = _sf.shapes()

    assert(len(shapes) > 0)
    _logger.info("Loaded {} shapes. ".format(len(shapes)))

    return shapes

shapes = load_shapes(FILENAME)
