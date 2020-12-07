# DAY 6: Advent Of Code 2020

inputFile = open('day7-input.txt', 'r')
luggageRules = inputFile.readlines()

# PART 1: count how many bag colors can carry a shiny gold bag

def countBagColors():
    colorsToCheck = ['shiny gold']
    bagColors = []

    while len(colorsToCheck) > 0:
        colorToCheck = colorsToCheck.pop()

        for (index, luggageRule) in enumerate(luggageRules):
            luggageRule = luggageRule.split(' bags contain')
            if colorToCheck in luggageRule[1]:
                colorsToCheck.append(luggageRule[0])
                bagColors.append(luggageRule[0])
        
    print len(set(bagColors))

# PART 2: count how many bags are in a shiny gold bag

def shinyGoldContains():
    colorsToCheck = ['shiny gold']
    countAllBags = 0

    while len(colorsToCheck) > 0:
        colorToCheck = colorsToCheck.pop()

        for (index, luggageRule) in enumerate(luggageRules):
            luggageRule = luggageRule.split(' bags contain ')
        
            if 'no other bags' in luggageRule[1]:
                continue
            
            if colorToCheck in luggageRule[0]:
                bagsInBag = luggageRule[1].split(', ')
                for bagInBag in bagsInBag:
                    bagInBagStringArray = bagInBag.split(' ')
                    numberOfBags = int(bagInBagStringArray[0])
                    countAllBags += numberOfBags

                    for i in range(numberOfBags):
                        colorsToCheck.append(bagInBagStringArray[1] + ' ' + bagInBagStringArray[2])
                    
                
    print countAllBags

countBagColors()
shinyGoldContains()

