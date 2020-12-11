# DAY 1: Advent Of Code 2020

inputFile = open('day1-input.txt', 'r')
numbers = inputFile.readlines()


# Finds two entries in inputFile that sum to 2020 and multiplies them
def twoNumbers():
    for x in numbers:
        for y in numbers:
            if int(x) + int(y) == 2020:
                result = int(x) * int(y)
                print('2020 = ', x, ' + ', y, ', result of multiplication: ', result)
                return

# Finds three entries in inputFile that sum to 2020 and multiplies them
def threeNumbers():
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if int(a) + int(b) + int(c) == 2020:
                    result = int(a) * int(b) * int(c)
                    print('2020 = ', a, ' + ', b, ' + ', c, ', result of multiplication: ', result)
                    return

twoNumbers()
threeNumbers()