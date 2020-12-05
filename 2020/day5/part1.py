import math

def computeValue(value, lowerBound, lowerChar, upperBound, upperChar):
    for c in value:
        diff = math.ceil((upperBound - lowerBound)/2)
        if c == lowerChar:
            upperBound -= diff
        elif c == upperChar:
            lowerBound += diff

    return upperBound if value[-1] == lowerChar else lowerBound

def genID(rowValue, seatValue):
    return (rowValue * 8) + seatValue

with open('./input','r') as fh:
    passes = fh.read().splitlines()
    passes = [(p[0:7],p[7:11]) for p in passes]
    seatIDs = []

    for bpass in passes:
        rowData, seatData = bpass

        rowValue = computeValue(rowData, 0, 'F', 127, 'B')
        seatValue = computeValue(seatData, 0, 'L', 7, 'R')
        seatID = genID(rowValue, seatValue)
        seatIDs.append(seatID)
    print(f'max seat id: {max(seatIDs)}')
