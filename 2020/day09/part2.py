inputFileName = 'input'
preambleSize = 25
def hasAddends(sum, preamble):
    addends = set()
    for pre in preamble:
        addend = sum - pre
        if addend in addends:
            return True
        else:
            addends.add(pre)
    return False

def findInvalidNumber(size, numbers):
    preamble = []
    for num in numbers:
        if len(preamble) == size:
            containsAddends = hasAddends(num, preamble)
            if containsAddends == False:
                return num 
            preamble.pop(0)
        preamble.append(num)
    return -1

with open(f'./{inputFileName}','r') as fh:
    numbers = [int(num) for num in fh]
    invalidNumber = findInvalidNumber(preambleSize, numbers)
    print(f'invalid number: {invalidNumber}')
    low = 0

    while low < len(numbers):
        sum = numbers[low]
        high = low + 1
        while high < len(numbers):
            sum += numbers[high]
            if sum >= invalidNumber:
                break
            high +=1

        if sum == invalidNumber:
            invalidNumAddends = numbers[low:high+1]
            small = min(invalidNumAddends)
            large = max(invalidNumAddends)
            print(small + large)
            break
        low += 1
