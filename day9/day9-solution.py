# DAY X: Advent Of Code 2020

inputFile = open('day9-input.txt', 'r')
numbers = inputFile.readlines()

# PART 1: find the first number in the input that is not a sum of any two of the X (=preamble) immediately previous numbers

def findRebelNumber():
    
    def checkSum(sumCandidates, sumCandidate):
        
        for i in range(len(sumCandidates) - 1):
            firstCandidate = int(sumCandidates[i])
            
            for j in range(i + 1, len(sumCandidates)):
                secondCandidate = int(sumCandidates[j])
                
                if firstCandidate + secondCandidate == sumCandidate:
                    return True
        
        return False

    preamble = 25

    for i in range(len(numbers) - (preamble+1)):
        candidatesArray = numbers[i: i + preamble + 1]
        sumCandidate = int(numbers[i + preamble + 1])
    
        isSumOfTwoNumbers = checkSum(candidatesArray, sumCandidate)

        if isSumOfTwoNumbers == False:
            print sumCandidate, ': is not a sum of any two of the numbers in the sumCandidates array'
            break

    # PART 2: find a contiguous set of at least two numbers that sum up to the invalid number
    for i in range(len(numbers)):
        sum = int(numbers[i])
        sumSet = [sum]

        for j in range(i + 1, len(numbers) - 1):
            sum += int(numbers[j])
            sumSet.append(int(numbers[j]))

            if sum == sumCandidate:
                sumSet = sorted(sumSet)
                result = sumSet[0] + sumSet[-1]
                print 'sum of min and max number in set is: ', result
                return

            elif sum > sumCandidate:
                break

findRebelNumber()
