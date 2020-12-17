from pprint import pprint
from copy import deepcopy
from math import ceil

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'

def countAdjOccSeats(map, rowIdx, seatIdx):
    deltas = [
        (-1, -1), # NORTH WEST
        (-1, 0),  # NORTH
        (-1, 1),  # NORTH EAST
        (0 , 1),  # EAST
        (1, 1),   # SOUTH EAST
        (1, 0),   # SOUTH
        (1, -1),  # SOUTH WEST
        (0, -1),  # WEST
    ]
    layersAway = ceil(max(len(map), len(map[0])))
    occSeats = 0
    for rowDelta, seatDelta in deltas:
        for layer in range(1, layersAway):
            adjRowIdx = rowIdx + (rowDelta * layer)
            adjSeatIdx = seatIdx + (seatDelta * layer)
            if not 0 <= adjRowIdx < len(map):
                # out of map stop going in this direction
                break 
            elif not 0 <= adjSeatIdx < len(map[0]):
                # out of map stop going in this direction
                break
            
            if map[adjRowIdx][adjSeatIdx] == FLOOR:
                # keep looking 
                continue
            elif map[adjRowIdx][adjSeatIdx] == EMPTY_SEAT:
                # stop looking
                break
            elif map[adjRowIdx][adjSeatIdx] == OCCUPIED_SEAT:
                # found occupied seat - stop looking
                occSeats += 1
                break

    return occSeats

with open(f'./input','r') as fh:
    map = [list(row.strip()) for row in fh.readlines()]

    occupiedSeats = {}
    itrCnt = 0
    while True:
        itrCnt +=1
        mapItr = deepcopy(map)
        for rowIdx, row in enumerate(map):
            for seatIdx, seat in enumerate(row):
                if seat == FLOOR:
                    continue

                adjOccSeats = countAdjOccSeats(map, rowIdx, seatIdx)
                # pprint(f'rowIdx: {rowIdx} seatIdx: {seatIdx} adjOccSeats: {adjOccSeats}')
                if seat == EMPTY_SEAT:
                    occupiedSeats[(rowIdx, seatIdx)] = False
                    if adjOccSeats == 0:
                        mapItr[rowIdx][seatIdx] = OCCUPIED_SEAT
                        occupiedSeats[(rowIdx, seatIdx)] = True 
                elif seat == OCCUPIED_SEAT:
                    occupiedSeats[(rowIdx, seatIdx)] = True
                    if adjOccSeats >= 5:
                        mapItr[rowIdx][seatIdx] = EMPTY_SEAT
                        occupiedSeats[(rowIdx, seatIdx)] = False
        if mapItr == map:
            break
        else:
            map = mapItr

    pprint(map)
    occupiedSeatCnt = sum(occupiedSeats.values())
    pprint(f'{occupiedSeatCnt} seats occupied')
