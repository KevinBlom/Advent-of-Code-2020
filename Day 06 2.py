from tools import *
testImport()

collectedAnswers = readFileToStrings("Input06")
groups = []
groupAnswers = []


def answerOfGroup(group):
    listOfSets = []
    for line in group:
        listOfSets.append(set(line))
    return len(listOfSets[0].intersection(*listOfSets))
    pass


for answerOfOnePerson in collectedAnswers:
    if answerOfOnePerson != "\n":
        groupAnswers.append(answerOfOnePerson.strip('\n'))
    else:
        groups.append(groupAnswers)
        groupAnswers = []

sumOfAnswers = 0

for group in groups:
    sumOfAnswers += answerOfGroup(group)

print(sumOfAnswers)
