requiredFields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
}

with open('./input','r') as fh:
    passports = fh.read().split('\n\n')
    validPasswordCnt = 0

    for passport in passports:
        passportParts = passport.replace('\n', ' ').split(' ')
        passportFields = [part.split(':')[0] for part in passportParts]

        if len(requiredFields.difference(set(passportFields))) == 0:
            validPasswordCnt += 1
    print(validPasswordCnt)
