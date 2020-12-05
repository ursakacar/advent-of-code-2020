# DAY 4: Advent Of Code 2020

import re

inputFile = open('day4-input.txt', 'r')
passports = inputFile.read()

# counting the # of valid passports without value validation

def validPassports1():
    requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validPassportsCount = 0
    passportsArray = passports.split('\n\n')
    for passport in passportsArray:
        passport = passport.replace('\n', ' ')
        passportFields = passport.split(' ')
        passportKeys = map(lambda field: field.split(':')[0], passportFields)
        result = list(set(requiredKeys) - set(passportKeys))
        if len(result) == 0:
            validPassportsCount += 1
    print 'Number of valid passports PART 1: ', validPassportsCount


# valid passports with value validation

def validPassports2():
    valuesValidation =  {
        'byr': lambda value: int(value) >= 1920 and int(value) <= 2002,
        'iyr': lambda value: int(value) >= 2010 and int(value) <= 2020,
        'eyr': lambda value: int(value) >= 2020 and int(value) <= 2030,
        'hgt': lambda value: ('cm' in value or 'in' in value) and
            (
                ('cm' in value and int(value.replace('cm', '')) >= 150 and int(value.replace('cm', '')) <= 193) or
                ('in' in value and int(value.replace('in', '')) >= 59 and int(value.replace('in', '')) <= 76)
            ),
        'hcl': lambda value: re.search(r'^#(?:[0-9a-f]{6})$', value),
        'ecl': lambda value: value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda value: re.search(r'^[0-9]{9}$', value)
    }
    requiredKeys = valuesValidation.keys()
    validPassportsCount = 0
    passportsArray = passports.split('\n\n')
    for passport in passportsArray:
        isPassportValid = True
        passport = passport.replace('\n', ' ')
        passportFields = passport.split(' ')
        for passportField in passportFields:            
            passportKey = passportField.split(':')[0]
            passportValue = passportField.split(':')[1]
            if passportKey in requiredKeys and not valuesValidation[passportKey](passportValue):
                isPassportValid = False
                break

        passportKeys = map(lambda field: field.split(':')[0], passportFields)
        result = list(set(requiredKeys) - set(passportKeys))
       
        if isPassportValid and len(result) == 0:    
            validPassportsCount += 1

    print 'Number of valid passports PART 2: ', validPassportsCount

validPassports1()
validPassports2()