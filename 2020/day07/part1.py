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
        for value in ruleValues:
            valueCnt, valueName = value

            if valueName in ruleMap:
                ruleMap[valueName].append((1/valueCnt, ruleKey))
            else:
                ruleMap[valueName] = [(1/valueCnt, ruleKey)] 

        rule = fh.readline().strip()

    bagsContainingTargetBag = findBagsWithTargetBag(ruleMap, [targetBag])
    print(len(bagsContainingTargetBag))
