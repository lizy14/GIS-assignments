
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
