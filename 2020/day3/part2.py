from math import prod
slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
]
treeMarker = '#'

with open('./input','r') as fh:
    map = fh.read().splitlines()
    yMax = len(map)
    xMax = len(map[0])
    treeCnts = []
    for slope in slopes:
        xDelta, yDelta = slope
        xPos = 0
        yPos = 0
        treeCnt = 0
        while yPos < (yMax - yDelta):
            yPos += yDelta
            xPos += xDelta

            if xPos >= xMax:
                xPos %= xMax

            currValue = map[yPos][xPos]
            if currValue == treeMarker:
                treeCnt += 1
        treeCnts.append(treeCnt)
    print(treeCnts)
    print(prod(treeCnts))
