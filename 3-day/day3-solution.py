# DAY 3: Advent Of Code 2020

inputFile = open('day3-input.txt', 'r')
area = inputFile.readlines()

# counting the trees(#) in the area pattern

def numberOfTrees():
    treeCountMultiplied = 1
    treeCountArray = []
    movePatternArray = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    for movePattern in movePatternArray:
        treeCount = 0
        position = 0
        for (lineIndex, line) in enumerate(area):
            if lineIndex % movePattern[1] != 0:
                continue

            lineLength = len(line.strip())
            position = position % lineLength

            if line[position] == '#':
                treeCount += 1
            
            position += movePattern[0]
            print(movePattern[0])
            
        treeCountArray.append(treeCount)

    for treeCount in treeCountArray:
        treeCountMultiplied *= treeCount
    
    print(treeCountArray)
    print(treeCountMultiplied)

numberOfTrees()