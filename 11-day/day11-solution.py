# DAY 11: Advent Of Code 2020
from copy import deepcopy

inputFile = open('day11-input.txt', 'r')
seats = inputFile.read().split('\n')

# this is so spaghetti that it hurts my eyes, but this one was tough & I'm just happy I FINALLY got it working

##### PART 1: How many seats are occupied after the chaos stabilizes?

def seatsOccupied():

    def countNeighbours(matrix, rowIndex, columnIndex, arrayToCheck):
        numberOfNeighbours = 0

        for i in range(len(arrayToCheck)):
            if matrix[rowIndex + arrayToCheck[i][0]][columnIndex + arrayToCheck[i][1]] == '#':
                numberOfNeighbours += 1

        return numberOfNeighbours

    def getNeighbours(row, column, numberOfRows, numberOfColumns):

        # count neighbours
        # corners 00
        if row == 0 and column == 0:
            neighbourArray = [[0, 1], [1, 0], [1, 1]]
        # corners 01
        elif row == 0 and column == numberOfColumns-1:
            neighbourArray = [[0, -1], [1, 0], [1, -1]]
        # corners 10
        elif row == numberOfRows-1 and column == 0:
            neighbourArray = [[-1, 0], [-1, 1], [0, 1]]
        # corners 11
        elif row == numberOfRows-1 and column == numberOfColumns-1:
            neighbourArray = [[-1, 0], [-1, -1], [0, -1]]
        # upper border
        elif row == 0:
            neighbourArray = [[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        # lower border`
        elif row == numberOfRows-1:
            neighbourArray = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1]]
        # left border
        elif column == 0:
            neighbourArray = [[-1, 0], [-1, 1], [0, 1], [1, 0], [1, 1]]
        # # right border
        elif column == numberOfColumns-1:
            neighbourArray = [[-1, -1], [-1, 0], [0, -1], [1, -1], [1, 0]]
        elif row != 0 and column != 0 and row != numberOfRows-1 and column != numberOfColumns-1:
            neighbourArray = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        return neighbourArray

    def getNewSittingOrder(sittingOrder):
        newSittingOrder = deepcopy(sittingOrder)

        for seatRowNumber, seatRow in enumerate(seats):
            for seatNumber, seat in enumerate(seatRow):

                neighbourArray = getNeighbours(seatRowNumber, seatNumber, len(seats), len(seatRow))
                numberOfNeighbours = countNeighbours(sittingOrder, seatRowNumber, seatNumber, neighbourArray)

                if sittingOrder[seatRowNumber][seatNumber] == '#' and numberOfNeighbours > 3:
                    newSittingOrder[seatRowNumber][seatNumber] = 'L'
                if sittingOrder[seatRowNumber][seatNumber] == 'L' and numberOfNeighbours == 0:
                    newSittingOrder[seatRowNumber][seatNumber] = '#'

        return newSittingOrder


    rows = len(seats)
    columns = len(seats[0])

    originalMatrix = [[0 for i in range(columns)] for y in range(rows)]

    for seatRowNumber, seatRow in enumerate(seats):
        for seatNumber, seat in enumerate(seatRow):
            originalMatrix[seatRowNumber][seatNumber] = seat

    newMatrix = getNewSittingOrder(originalMatrix)

    while newMatrix != originalMatrix:
        originalMatrix = deepcopy(newMatrix)
        newMatrix = getNewSittingOrder(newMatrix)

    # count seats after the matrix has converged
    seatCounter = 0
    for seatRowNumber, seatRow in enumerate(seats):
        for seatNumber, seat in enumerate(seatRow):
            if originalMatrix[seatRowNumber][seatNumber] == '#':
                seatCounter += 1

    # print newMatrix
    print 'Part 1: number of occupied seats: ', seatCounter


##### PART 2: the same, but counting seats diagonally

def diagonalSeatsOccupied():

    def countNeighbours(matrix, rowIndex, columnIndex, arrayToCheck):
        numberOfNeighbours = 0

        for i in range(len(arrayToCheck)):
            multiplier = 1
            rowIndexToCheck = rowIndex + arrayToCheck[i][0]
            columnIndexToCheck = columnIndex + arrayToCheck[i][1]

            while rowIndexToCheck >= 0 and columnIndexToCheck >= 0 and rowIndexToCheck < len(matrix) and columnIndexToCheck < len(matrix[0]):
                if matrix[rowIndexToCheck][columnIndexToCheck] == '#':
                    numberOfNeighbours += 1
                    break
                elif matrix[rowIndexToCheck][columnIndexToCheck] == 'L':
                    break
                multiplier += 1
                rowIndexToCheck = rowIndex + arrayToCheck[i][0] * multiplier
                columnIndexToCheck = columnIndex + arrayToCheck[i][1] * multiplier

        return numberOfNeighbours

    def getNeighbours(row, column, numberOfRows, numberOfColumns):

        # count neighbours
        # corners 00
        if row == 0 and column == 0:
            neighbourArray = [[0, 1], [1, 0], [1, 1]]
        # corners 01
        elif row == 0 and column == numberOfColumns-1:
            neighbourArray = [[0, -1], [1, 0], [1, -1]]
        # corners 10
        elif row == numberOfRows-1 and column == 0:
            neighbourArray = [[-1, 0], [-1, 1], [0, 1]]
        # corners 11
        elif row == numberOfRows-1 and column == numberOfColumns-1:
            neighbourArray = [[-1, 0], [-1, -1], [0, -1]]
        # upper border
        elif row == 0:
            neighbourArray = [[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        # lower border`
        elif row == numberOfRows-1:
            neighbourArray = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1]]
        # left border
        elif column == 0:
            neighbourArray = [[-1, 0], [-1, 1], [0, 1], [1, 0], [1, 1]]
        # # right border
        elif column == numberOfColumns-1:
            neighbourArray = [[-1, -1], [-1, 0], [0, -1], [1, -1], [1, 0]]
        elif row != 0 and column != 0 and row != numberOfRows-1 and column != numberOfColumns-1:
            neighbourArray = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        return neighbourArray

    def getNewSittingOrder(sittingOrder):
        newSittingOrder = deepcopy(sittingOrder)

        for seatRowNumber, seatRow in enumerate(seats):
            for seatNumber, seat in enumerate(seatRow):

                neighbourArray = getNeighbours(seatRowNumber, seatNumber, len(seats), len(seatRow))
                numberOfNeighbours = countNeighbours(sittingOrder, seatRowNumber, seatNumber, neighbourArray)

                if sittingOrder[seatRowNumber][seatNumber] == '#' and numberOfNeighbours > 4:
                    newSittingOrder[seatRowNumber][seatNumber] = 'L'
                if sittingOrder[seatRowNumber][seatNumber] == 'L' and numberOfNeighbours == 0:
                    newSittingOrder[seatRowNumber][seatNumber] = '#'

        return newSittingOrder

    rows = len(seats)
    columns = len(seats[0])

    originalMatrix = [[0 for i in range(columns)] for y in range(rows)]

    for seatRowNumber, seatRow in enumerate(seats):
        for seatNumber, seat in enumerate(seatRow):
            originalMatrix[seatRowNumber][seatNumber] = seat

    newMatrix = getNewSittingOrder(originalMatrix)
    # print newMatrix
    while newMatrix != originalMatrix:
        originalMatrix = deepcopy(newMatrix)
        newMatrix = getNewSittingOrder(newMatrix)

    # count seats after the matrix has converged
    seatCounter = 0
    for seatRowNumber, seatRow in enumerate(seats):
        for seatNumber, seat in enumerate(seatRow):
            if originalMatrix[seatRowNumber][seatNumber] == '#':
                seatCounter += 1

    # print newMatrix
    print 'Part 2: Number of occupied seats: ', seatCounter

seatsOccupied()
diagonalSeatsOccupied()
