from dao import shapes


def test_mbr():
    for shape in shapes:
        assert(str(shape.bbox) == str(mbr(shape)))


def mbr(shape):
    minX = float('inf')
    minY = minX
    maxX = float('-inf')
    maxY = maxX

    for point in shape.points:
        x = point[0]
        y = point[1]
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y
    return [minX, minY, maxX, maxY]


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
            print ('shape # {} does not exist! '.format(shapeid))
            continue

        print minimal_bounding_rectangle(shape)


if __name__ == "__main__":
    main()
