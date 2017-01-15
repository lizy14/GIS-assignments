from dao import *
from graph import *
from geometry import *
from config import *


def input_point(desc):
    x = raw_input("{} x> ".format(desc))
    y = raw_input("{} y> ".format(desc))
    x = float(x)
    y = float(y)
    return (x, y)


def main():
    shapes = load_shapes(FILENAME)
    g = build_graph(shapes)
    start = input_point('starting point')
    end = input_point('ending point')
    print(shortest_path_wrapped(shapes, g, start, end))

if __name__ == '__main__':
    main()
