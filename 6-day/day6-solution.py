# DAY 6: Advent Of Code 2020

inputFile = open('day6-input.txt', 'r')
customsDeclarationAnswers = inputFile.read().split('\n\n')

# PART 1: count the unique occurences of characters in each answer group

def countUniqueAnswers():
    uniqueAnswerCount = 0
    answersGroupArray = []

    for answerGroup in customsDeclarationAnswers:
        answersGroupArray.append(answerGroup.replace("\n", ""))

    for answerGroup in answersGroupArray:
        uniqueAnswerCount += len(set(answerGroup))
    print uniqueAnswerCount

countUniqueAnswers()

# PART 2: count the characters that appear on all lines within each answer group

def countSameAnswers():
    sameAnswerCount = 0

    for answersGroup in customsDeclarationAnswers:
        answers = answersGroup.split('\n')
        sameAnswer = set(answers[0])

        for answer in answers[1:]:
            sameAnswer = sameAnswer.intersection(answer)
        sameAnswerCount += len(sameAnswer)
    
    print sameAnswerCount

countSameAnswers()
