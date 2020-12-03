xDelta = 3
yDelta = 1
treeMarker = '#'

with open('./input','r') as fh:
    map = fh.read().splitlines()
    yMax = len(map)
    xMax = len(map[0])

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
    print(treeCnt)
