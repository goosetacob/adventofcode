import re

with open('./input','r') as fh:
    passwordRecords = fh.read().splitlines()
    passwordRecords = [re.split(r'^(\d+)\-(\d+)\s(\w):\s(\w+)$',pwd)[1:-1] for pwd in passwordRecords]
    validPasswordsCnt = 0
    for record in passwordRecords:
        firstIdx, secondIdx, char, password = record
        passwordLength = len(password)

        # account for zero indexing
        firstIdx = int(firstIdx) - 1
        secondIdx = int(secondIdx) - 1

        firstChar = password[firstIdx] if firstIdx < passwordLength else 'null'
        secondChar = password[secondIdx] if secondIdx < passwordLength else 'null'

        # skip if they're the same 
        if firstChar == secondChar:
            continue

        # skip if either is out of range
        if firstChar == 'null' or secondChar == 'null':
            continue
        
        # skip if neither is the target character
        if firstChar != char and secondChar != char:
            continue

        validPasswordsCnt += 1

    print(validPasswordsCnt)
