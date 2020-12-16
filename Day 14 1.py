from tools import *
testImport()

lines = readFileToStrings("Input14")

sumOfAllValuesInMemory = 0
mask = ''

dictOfValues = {}


def retrieveMask(line):
    return line[7:]
    pass


def retrieveValue(line):
    return int(line[line.find('=') + 2:])
    pass


def retrieveMemoryLocation(line):
    return line[line.find('[') + 1:line.find(']')]
    pass


def applyMask(value, mask):
    formattedValue = '{0:036b}'.format(value)

    valueAsList = [char for char in str(formattedValue)]

    for i in range(0, len(mask) - 1):
        if mask[i] == 'X':
            continue
        else:
            valueAsList[i] = mask[i]

    return int(''.join(valueAsList), 2)
    pass


for line in lines:
    if line[1] == 'a':
        mask = retrieveMask(line)
    if line[1] == 'e':
        memoryLocation = retrieveMemoryLocation(line)
        value = retrieveValue(line)
        value = applyMask(value, mask)
        dictOfValues[memoryLocation] = value


for key in dictOfValues:
    sumOfAllValuesInMemory += dictOfValues[key]

print(sumOfAllValuesInMemory)
