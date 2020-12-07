from tools import *
from collections import defaultdict
testImport()

collectedAnswers = readFileToStrings("Input06")
groups = []
groupAnswers = []


def uniqueAnswersOfGroup(group):
    return len(set(''.join(group)))
    pass


for answerOfOnePerson in collectedAnswers:
    if answerOfOnePerson != "\n":
        groupAnswers.append(answerOfOnePerson.strip('\n'))
    else:
        groups.append(groupAnswers)
        groupAnswers = []

sumOfUniqueAnswers = 0

for group in groups:
    sumOfUniqueAnswers += uniqueAnswersOfGroup(group)

print(sumOfUniqueAnswers)
