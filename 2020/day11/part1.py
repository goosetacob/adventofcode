from pprint import pprint
from copy import deepcopy

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
    occSeats = 0
    for rowDelta, seatDelta in deltas:
        adjRowIdx = rowIdx + rowDelta
        adjSeatIdx = seatIdx + seatDelta
        
        if not 0 <= adjRowIdx < len(map):
            continue
        elif not 0 <= adjSeatIdx < len(map[0]):
            continue
        
        if map[adjRowIdx][adjSeatIdx] == OCCUPIED_SEAT:
            occSeats += 1

    return occSeats

with open(f'./input','r') as fh:
    map = [list(row.strip()) for row in fh.readlines()]

    occupiedSeats = {}
    itrCnt = 0
    while True:
        itrCnt +=1
        pprint(f'itrCnt: {itrCnt}')
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
                    if adjOccSeats >= 4:
                        mapItr[rowIdx][seatIdx] = EMPTY_SEAT
                        occupiedSeats[(rowIdx, seatIdx)] = False
        if mapItr == map:
            break
        else:
            map = mapItr

    pprint(map)
    occupiedSeatCnt = sum(occupiedSeats.values())
    pprint(f'{occupiedSeatCnt} seats occupied')
