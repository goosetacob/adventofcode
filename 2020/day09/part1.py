inputFileName = 'input'

def hasAddends(sum, preamble):
    addends = set()
    for pre in preamble:
        addend = sum - pre
        if addend in addends:
            return True
        else:
            addends.add(pre)
    return False

with open(f'./{inputFileName}','r') as fh:
    preambleSize = 25
    preamble = []
    for num in fh:
        num = int(num)
        
        if len(preamble) == preambleSize:
            containsAddends = hasAddends(num, preamble)
            if containsAddends == False:
                print(f'{num} does not have addends in {preamble}')
            preamble.pop(0)

        preamble.append(num)
