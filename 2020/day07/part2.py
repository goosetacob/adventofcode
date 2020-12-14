from pprint import pprint
inputFileName = 'input'
targetBag = 'shiny gold'

def parseRule(rule):
    ruleKey, ruleValues = rule.rstrip('.').split(' contain ')

    # clean keys
    key = ruleKey.removesuffix(' bags')

    # clean values
    values = []
    if (ruleValues == 'no other bags'):
        return (key, values)

    ruleValues = ruleValues.split(', ')
    for v in ruleValues:
        parts = v.split(' ') 
        vCnt = int(parts[0])
        vName = ' '.join(parts[1:-1])
        values.append((vCnt, vName))

    return (key, values)

def countNestedBags(bagsMap, bag, quantity):
    if not bag in bagsMap:
        return 0

    total = 0
    nextBags = bagsMap[bag]
    for nBag in nextBags:
        nQuantity, nName = nBag
        nestedCount = countNestedBags(bagsMap, nName, nQuantity)
        nestedCount *= quantity
        total += nestedCount
    return total + quantity

def findBagsWithTargetBag(bagsMap, targets):
    encounteredBags = set()
    while len(targets):
        target = targets.pop()

        if not target in bagsMap:
            print(f'{target} not in map')
            continue

        next = bagsMap[target]
        for n in next:
            _, name = n
            encounteredBags.add(name)
            targets.append(name)

    return encounteredBags

with open(f'./{inputFileName}','r') as fh:
    rule = fh.readline().strip()
    ruleCnt = 0
    ruleMap = {}
    while rule:
        ruleCnt += 1
        ruleKey, ruleValues = parseRule(rule)
        ruleMap[ruleKey] = ruleValues
        rule = fh.readline().strip()

    bagsCount = countNestedBags(ruleMap, targetBag, 1)
    # exclude first target bag
    bagsCount -= 1
    print(f'nested bags count: {bagsCount}')
