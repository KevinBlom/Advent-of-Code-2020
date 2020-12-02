from tools import *
testImport()


def extractPolicyPositions(line):
    explodedString = line.split()
    positions = explodedString[0]
    firstPosition = positions.split("-")[0]
    secondPosition = positions.split("-")[1]
    return int(firstPosition) - 1, int(secondPosition) - 1


def extractMandatoryChar(line):
    explodedString = line.split()
    char = explodedString[1][0]
    return char


def extractPassword(line):
    explodedString = line.split()
    password = explodedString[2]
    return password


def evaluatePolicy(line):
    first, second = extractPolicyPositions(line)
    print(first, second)
    char = extractMandatoryChar(line)
    password = extractPassword(line)
    countOfChars = password.count(char)
    return (password[first] == char) ^ (password[second] == char)


testInput = ["1-3 a: abcde",
             "1-3 b: cdefg"
             "2-9 c: ccccccccc"]

lines = readFileToStrings("Input02")

validPasswords = 0

for line in lines:
    if evaluatePolicy(line):
        validPasswords += 1

print(validPasswords)
