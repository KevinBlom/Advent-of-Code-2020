from tools import *
import math

lines = readFileToStrings("Input03")

space = "."
tree = "#"

slopes = [[1, 1],
          [3, 1],
          [5, 1],
          [7, 1],
          [1, 2]]

arrayOfTreecount = []


def evaluatePosition(char):
    if char == space:
        return 0
    elif char == tree:
        return 1
    else:
        return -10000


def runWithSlope(horizontalStep, verticalStep):
    countOfTrees = 0
    xPos = 0
    yPos = 0
    for line in lines:

        if (yPos % verticalStep != 0):
            yPos += 1
            continue

        countOfTrees += evaluatePosition(line[xPos])

        xPos += horizontalStep
        yPos += 1
        if xPos >= (len(line) - 1):
            xPos = xPos % (len(line) - 1)

    return countOfTrees


for slope in slopes:
    arrayOfTreecount.append(runWithSlope(slope[0], slope[1]))

print(math.prod(arrayOfTreecount))
