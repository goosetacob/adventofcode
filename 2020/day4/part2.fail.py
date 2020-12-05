from re import match

def validateHeight(value):
    height_match = match(r'^(\d+)(in|cm)$', value)
    if not height_match:
        return False

    height, unit= height_match.groups()
    if unit == 'cm' and not 150 <= int(height) <= 193:
        return False
    if unit == 'in' and not 59 <= int(height) <= 76:
        return False

    return True

validations = {
    'byr': lambda value: 1920 <= int(value) <= 2002,
    'iyr': lambda value: 2010 <= int(value) <= 2020,
    'eyr': lambda value: 2020 <= int(value) <= 2030,
    'hgt': validateHeight,
    'hcl': lambda value: match(r'^#[0-9a-f]{6}$', value),
    'ecl': lambda value: value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda value: match(r'^\d{9}$', value),
}

def parsePassport(rawData):
    passportData = {}
    dataFields = rawData.strip().replace('\n', ' ').split(' ')
    for field in dataFields:
        fieldParts = field.split(':')
        passportData[fieldParts[0]] = fieldParts[1]
    return passportData

with open('./input','r') as fh:
    validPassportCnt = 0
    invalidPassportCnt = 0
    requiredFields = validations.keys()

    rawPassports = fh.read().split('\n\n')
    for rawData in rawPassports:
        passportData = parsePassport(rawData)

        validPassport = True
        for req in requiredFields:
            if req in passportData:
                validationFn = validations[req]
                passportValue = passportData[req]

                if req == 'iyr':
                    print(f'{req} {not validationFn(passportValue)} {passportValue}')

                if not validationFn(passportValue):
                    validPassport = False
                    break
            else:
                validPassport = False
                break
        
        if validPassport:
            validPassportCnt += 1
        else:
            invalidPassportCnt += 1

    print(f'valid: {validPassportCnt}')
    print(f'invalid: {invalidPassportCnt}')
    print(f'total: {validPassportCnt + invalidPassportCnt}')
    print(len(rawPassports))
    
