from tools import *
testImport()

adapters = readFileToStrings("Input10")

adapters = list(map(lambda x: int(x.strip()), adapters))
adapters.sort()

print(adapters)

oneJoltCount = 0
threeJoltCount = 0

for i in range(0, len(adapters) - 1):
    joltDifference = adapters[i + 1] - adapters[i]

    if joltDifference == 1:
        oneJoltCount += 1
    elif joltDifference == 3:
        threeJoltCount += 1
    else:
        print("Error")

print(oneJoltCount * threeJoltCount)
