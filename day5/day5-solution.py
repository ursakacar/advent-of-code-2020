# DAY 5: Advent Of Code 2020

inputFile = open('day5-input.txt', 'r')
boardingPasses = inputFile.readlines()

# highest boarding pass ID & the ID of your seat

def boardingPassID():
    maxSeatID = 0 # would not be needed as we have an array in part 2 of the puzzle, but I'm leaving it in, because no reason :)
    seatIDArray = []
    for boardingPass in boardingPasses:
        rows = boardingPass[0:7]
        rows = rows.replace('F', '0')
        rows = rows.replace('B', '1')
        columns = boardingPass[7:10]
        columns = columns.replace('L', '0')
        columns = columns.replace('R', '1')

        rowNumber = 0
        columnNumber = 0

        for (index, row) in enumerate(rows):
            rowNumber += int(row) * 2 ** (6 - index)

        for (index, column) in enumerate(columns):
            columnNumber += int(column) * 2 ** (2 - index)

        seatID = rowNumber * 8 + columnNumber
        seatIDArray.append(seatID)
        
        if seatID > maxSeatID: # again, is not really needed as we have an arreay of seatID's with part 2 of the puzzle, but I'm leaving it in
            maxSeatID = seatID
    
    seatIDArray = sorted(seatIDArray)

    for (index, seat) in enumerate(seatIDArray):
        if not seatIDArray[index+1] == int(seat) + 1:
            yourSeatID = int(seat) + 1
            break

    print 'Max seat ID: ', maxSeatID
    print 'Your seat ID: ', yourSeatID

boardingPassID()