from collections import defaultdict
from progress import printProgress
import logging
from config import DEBUG
logging.basicConfig(level=DEBUG)
_logger = logging.getLogger(__name__)


# reference: https://gist.github.com/econchick/4666413
class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def dijsktra(graph, initial):
        _logger.debug("dijsktra {}".format(initial))
        _total = len(graph.nodes)

        visited = {initial: 0}
        path = {}

        nodes = set(graph.nodes)

        while nodes:

            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:
                weight = current_weight + graph.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
                    printProgress(len(visited), _total)

        printProgress(1, 1)
        _logger.debug("dijsktra finished")

        return visited, path


def shortest_path(graph, start, end):
    (reachable, precursor) = graph.dijsktra(start)
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


def test_graph():
    g = Graph()
    g.add_node(4)
    g.add_node(5)
    g.add_node(8)
    g.add_edge(4, 8, 4)
    g.add_edge(5, 8, 2)
    g.add_node(6)
    assert(shortest_path(g, 5, 4) == [5, 8, 4])
    g.add_edge(5, 6, 2)
    g.add_edge(4, 6, 1)
    assert(shortest_path(g, 5, 4) == [5, 6, 4])
    g.add_edge(4, 5, 1.4)
    assert(shortest_path(g, 5, 4) == [5, 4])
