from math import sqrt
import logging
from config import DEBUG
logging.basicConfig(level=DEBUG)
_logger = logging.getLogger(__name__)


def euclidean_distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    sq = dx ** 2 + dy ** 2
    return sqrt(sq)


def path_length(points):
    distance = 0
    for i in range(len(points) - 1):
        a = points[i]
        b = points[i + 1]
        distance += euclidean_distance(a, b)
    return distance


def test_path_length():
    assert(path_length([(0, 0), (1, 1), (2, 3)]) == sqrt(2) + sqrt(5))


def nearest_neighbor(points, p):
    nearest = None
    minimal_distance = float('inf')
    for point in points:
        distance = euclidean_distance(p, point)
        if distance < minimal_distance:
            minimal_distance = distance
            nearest = point
    _logger.debug('nearest neighboor {}'.format(nearest))
    return nearest
