from dao import shapes
while True:
    shapeid = raw_input('shape id> ')
    try:
        shapeid = int(shapeid)
    except ValueError:
        break

    try:
        shape = shapes[shapeid]
    except IndexError:
        print ('shape with specified id {} does not exist! '.format(shapeid))
        continue

    print (shape.bbox)
