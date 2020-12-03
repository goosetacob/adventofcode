import re

with open('./input','r') as fh:
    passwordRecords = fh.read().splitlines()
    passwordRecords = [re.split(r'^(\d+)\-(\d+)\s(\w):\s(\w+)$',pwd)[1:-1] for pwd in passwordRecords]
    validPasswordsCnt = 0
    for record in passwordRecords:
        min, max, char, password = record
        charCnt = password.count(char)
        if int(min) <= charCnt and charCnt <= int(max):
            validPasswordsCnt += 1
    print(validPasswordsCnt)
