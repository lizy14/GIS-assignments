from graph import *
from geometry import *
import logging
from config import DEBUG
logging.basicConfig(level=DEBUG)
_logger = logging.getLogger(__name__)


def build_graph(shapes):
    g = Graph()
    _logger.info("Building graph...")
    for shape in shapes:
        points = shape.points
        start = points[0]
        end = points[-1]
        distance = path_length(points)

        g.add_node(start)
        g.add_node(end)
        g.add_edge(start, end, distance)

    _logger.info("Graph built with {} nodes.".format(len(g.nodes)))
    return g


def main():
    from dao import shapes
    g = build_graph(shapes)
    _logger.debug(
        shortest_path(
            g,
            nearest_neighbor(g.nodes, (600, 400)),
            nearest_neighbor(g.nodes, (400, 600)),
        )
    )

if __name__ == '__main__':
    main()
