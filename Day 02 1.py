from tools import *
testImport()


def extractPolicyMinMax(line):
    explodedString = line.split()
    minMax = explodedString[0]
    min = minMax.split("-")[0]
    max = minMax.split("-")[1]
    return int(min), int(max)
    pass


def extractMandatoryChar(line):
    explodedString = line.split()
    char = explodedString[1][0]
    return char


def extractPassword(line):
    explodedString = line.split()
    password = explodedString[2]
    return password


def evaluatePolicy(line) -> bool:
    min, max = extractPolicyMinMax(line)
    char = extractMandatoryChar(line)
    password = extractPassword(line)
    countOfChars = password.count(char)
    return min <= countOfChars <= max


testInput = ["1-3 a: abcde",
             "1-3 b: cdefg"
             "2-9 c: ccccccccc"]

lines = readFileToStrings("Input02")

validPasswords = 0

for line in lines:
    if evaluatePolicy(line):
        validPasswords += 1

print(validPasswords)
