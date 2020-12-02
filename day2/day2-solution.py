# DAY 2: Advent Of Code 2020

# Each line in the input file has its password policy and the password

inputFile = open('day2-input.txt', 'r')
passwords = inputFile.readlines()

# Prints the number of valid passwords in the inputFile
# Password policy: indicates the lowest and highest number of times a given letter must appear for the password to be valid

def validPasswordsPart1(): 
    numberOfValidPasswords = 0
    for line in passwords:
        letterRepeatRange = line.split()[0].split('-')
        letter = line.split(':')[-2][-1]
        password = line.split()[-1]
        letterCount = 0

        for char in range(0, len(password)):
            if password[char] == letter:
                letterCount += 1
        
        if (letterCount >= int(letterRepeatRange[0]) and letterCount <= int(letterRepeatRange[1])):
                numberOfValidPasswords += 1

    print('Number of valid passwords in part 1: ', numberOfValidPasswords)

# Prints the number of valid passwords in the inputFile
# Password policy: indicates exact two positions, where only ONE of them HAS to contain the given letter in order for the password to be valid

def validPasswordsPart2(): 
    numberOfValidPasswords = 0
    for line in passwords:
        letterRepeatRange = line.split()[0].split('-')
        letter = line.split(':')[-2][-1]
        password = line.split()[-1]
        firstLetterPosition = int(letterRepeatRange[0]) - 1
        secondLetterPosition = int(letterRepeatRange[1]) - 1

        if (letter == password[firstLetterPosition]) ^ (letter == password[secondLetterPosition]):
            numberOfValidPasswords += 1

    print('Number of valid passwords in part 2: ', numberOfValidPasswords)

validPasswordsPart1()
validPasswordsPart2()