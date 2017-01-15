from math import sqrt
from progress import printProgress
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


def shortest_path_wrapped(shapes, graph, start, end, progress=printProgress):
    start = nearest_neighbor(graph.nodes, start)
    end = nearest_neighbor(graph.nodes, end)
    path = shortest_path(graph, start, end, progress)

    def path_between_adjacent_nodes(shapes, start, end):
        def directly_connects(line, start, end):
            if line.points[0] == start and line.points[-1] == end:
                return True
            if line.points[-1] == start and line.points[0] == end:
                return True
            return False
        return filter(lambda x: directly_connects(x, start, end), shapes)

    result = []
    for i in range(len(path) - 1):
        candidates = path_between_adjacent_nodes(shapes, path[i], path[i + 1])
        shortest = min(candidates, key=lambda x: path_length(x.points))
        shortest = shortest.points
        if shortest[0] != start:
            shortest.reverse()
        result += shortest
    _logger.debug('shortest_path: ' + str(result))
    return result


def shortest_path(graph, start, end, progress=printProgress):
    (reachable, precursor) = graph.dijsktra(start, progress)
    if end not in reachable:
        raise Exception("node unreachable")

    path = []
    cursor = end
    while True:
        path.append(cursor)
        cursor = precursor[cursor]
        if(cursor == start):
            break

    path.append(start)
    path.reverse()
    return path
