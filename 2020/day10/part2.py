from pprint import pprint

with open(f'./input','r') as fh:
    adapters = fh.readlines()
    adapters = [ int(aj.strip()) for aj in adapters]
    adapters.sort()
    builtInAdapter = adapters[-1] + 3 
    adapters = [0] + adapters + [builtInAdapter]
    adapterPos = { adapters[i] : i for i in range(0, len(adapters) ) }

    # count the possible adaptors adaptor-N can plug into
    # adapters = [ ..., N-1, N, N+1]
    # explanation that helped me: https://www.twitch.tv/videos/832019096
    ways = [1] * len(adapters)
    for adapterIdx in range(len(adapters) - 2, -1, -1):
        # get adaptorN
        currAdapter = adapters[adapterIdx]
        waysToCurrAdapter = 0

        # adaptorN can plug into adaptors with joltages +1, +2, +3
        for diff in [1, 2, 3]:
            potentialAdapter = currAdapter + diff
            if potentialAdapter in adapterPos:
                # if potential adaptor exists
                # get the number of adaptors it can plug into
                # add them into the count of adaptors adaptorN can plug into
                potentialAdapterIdx = adapterPos[potentialAdapter]
                waysToCurrAdapter += ways[potentialAdapterIdx]

        # store how many adaptors, adaptorN can plug into
        ways[adapterIdx] = waysToCurrAdapter

    # sum the number of adaptors, adaptors with values of 3,2,1 can plug into
    # only care about adaptors with joltages 3,2,1 because they are the limiting values
    pprint(ways)
    cnt = 0
    for diff in [1, 2, 3]:
        if diff in adapterPos:
            adapterIdx = adapterPos[diff]
            waysToAdapter = ways[adapterIdx]
            cnt += waysToAdapter 
    pprint(cnt)
