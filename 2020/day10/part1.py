from pprint import pprint
with open(f'./input','r') as fh:
    adapterJolts = fh.readlines()
    adapterJolts = [ int(aj.strip()) for aj in adapterJolts]
    adapterJolts.sort()
    adapterJolts.append(adapterJolts[-1] + 3)

    startingJolts = 0
    diffCounts = {}
    for jolts in adapterJolts:
        diff = jolts - startingJolts
        startingJolts = jolts
        if diff in diffCounts:
            diffCounts[diff] += 1
        else:
            diffCounts[diff] = 1

    magicNumber = diffCounts[1] * diffCounts[3]
    pprint(f'diffCounts: {diffCounts}')
    pprint(f'magic number: {magicNumber}')
