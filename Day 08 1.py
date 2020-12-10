from tools import *
testImport()

inputInstructions = readFileToStrings("Input08")

instructions = []


def executeInstruction(operation, argument, position, accumulator):
    if operation == 'acc':
        accumulator += argument
        position += 1
    if operation == 'jmp':
        position += argument
    if operation == 'nop':
        position += 1
    return position, accumulator


for instruction in inputInstructions:
    operation = instruction.strip().split()[0]
    argument = int(instruction.strip().split()[1])
    instructions.append([operation, argument])

position = 0
accumulator = 0
visitedPositions = set()
loopFound = False

while not loopFound:
    if position in visitedPositions:
        loopFound = True
    else:
        visitedPositions.add(position)
        operation, argument = instructions[position]
        position, accumulator = executeInstruction(
            operation, argument, position, accumulator)


print(accumulator)
