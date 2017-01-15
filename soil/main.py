from dao import shapes
from mbr import *


def main():

    while True:
        shapeid = raw_input('shape id> ')

        try:
            shapeid = int(shapeid)
        except ValueError:
            break

        try:
            shape = shapes[shapeid]
        except IndexError:
            print('shape # {} does not exist! '.format(shapeid))
            continue

        print(mbr(shape))


if __name__ == "__main__":
    main()
