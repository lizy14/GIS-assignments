from unittest import TestCase, main
from geometry import *
from graph import *


class TestGeometry(TestCase):

    def test_euclidean_distance(_):
        assert(euclidean_distance((1, 1), (3, 4)) == sqrt(4 + 9))

    def test_path_length(_):
        assert(path_length([(0, 0), (1, 1), (2, 3)]) == sqrt(2) + sqrt(5))

    def test_nearest_neighbor(_):
        pass


class TestGraph(TestCase):

    def test_graph(_):
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


if __name__ == '__main__':
    main()
