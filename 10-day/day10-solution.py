# DAY 10: Advent Of Code 2020

inputFile = open('day10-input.txt', 'r')
adapters = inputFile.read().split('\n')

adaptersSorted = sorted([int(adapter) for adapter in adapters])

# PART 1: chain the adapters

def adaptersChain():
    oneJolt = 0
    twoJolt = 0
    threeJolt = 1

    if adaptersSorted[0] == 1:
        oneJolt += 1
    elif adaptersSorted[0] == 2:
        threeJolt += 1
    elif adaptersSorted[0] == 3:
        threeJolt += 1
    else:
        print 'difference too big'

    for (index, adapter) in enumerate(adaptersSorted):
        if index == len(adaptersSorted) - 1: 
            continue

        if adaptersSorted[index + 1] - adaptersSorted[index] == 1:
            oneJolt += 1

        elif adaptersSorted[index + 1] - adaptersSorted[index] == 2:
            twoJolt += 1

        elif adaptersSorted[index + 1] - adaptersSorted[index] == 3:
            threeJolt += 1

    print 'multiplier of 1-jolt diff count and 3 jolt diff count:', oneJolt * threeJolt 

# PART 2: find all possible adapters combination

def adaptersCombination():

    combinationsPerAdapter = {0:1}

    for adapter in adaptersSorted:
        # for each adapter we need a number of how many of the 3 adapters BEFORE it can connect to that adapter, and then sum that number
        correctAdaptersCount = 0

        if adapter - 1 in combinationsPerAdapter:
            correctAdaptersCount += combinationsPerAdapter[adapter-1]
        if adapter - 2 in combinationsPerAdapter:
            correctAdaptersCount += combinationsPerAdapter[adapter-2]
        if adapter - 3 in combinationsPerAdapter:
            correctAdaptersCount += combinationsPerAdapter[adapter-3]
        
        combinationsPerAdapter[adapter] = correctAdaptersCount
        
    print 'the number of all possible combinations: ', combinationsPerAdapter[max(adaptersSorted)]

adaptersChain()
adaptersCombination()
