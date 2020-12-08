# DAY 8: Advent Of Code 2020

inputFile = open('day8-input.txt', 'r')
gameInstructions = inputFile.readlines()

# PART 1: find the infinite loop

def findInfiniteLoop():
    accumulator = 0
    index = 0
    visitedIndexes = []

    while True:
        line = gameInstructions[index].replace('\n', '').split(' ')
        
        if index in visitedIndexes:
            print 'Program looped. Accumulator value: ', accumulator
            return

        visitedIndexes.append(index)
        
        step = line[0]
        stepNumber = line[1]

        if step == 'nop':
            index += 1
        elif step == 'acc':
            accumulator += int(stepNumber)
            index += 1
        elif step == 'jmp':
            index += int(stepNumber)
        
# PART 2: fix infinite loop

def fixInfiniteLoop():
    
    def gameResult(gameFixedInstructions):
        print 'fixed', gameFixedInstructions
        print 'orig', gameInstructions
        accumulator = 0
        index = 0
        visitedIndexes = []

        while index < len(gameFixedInstructions):
            line = gameFixedInstructions[index].replace('\n', '').split(' ')
            
            if index in visitedIndexes:
                return False

            visitedIndexes.append(index)
            
            step = line[0]
            stepNumber = line[1]

            if step == 'nop':
                index += 1
            elif step == 'acc':
                accumulator += int(stepNumber)
                index += 1
            elif step == 'jmp':
                index += int(stepNumber)
        
        return accumulator

    for (index, line) in enumerate(gameInstructions):
        result = False
        if 'nop' in line:
            fixedLines = list(gameInstructions)
            fixedLines[index] = fixedLines[index].replace('nop', 'jmp')
            result = gameResult(fixedLines)
        elif 'jmp' in line:
            fixedLines = list(gameInstructions)
            fixedLines[index] = fixedLines[index].replace('jmp', 'nop')
            result = gameResult(fixedLines)

        if result:
            print 'Program terminated! Accumulator: ', result 
            return
        
findInfiniteLoop()
fixInfiniteLoop()

