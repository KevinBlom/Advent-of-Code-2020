from tools import *
import math
testImport()

boardingPasses = readFileToStrings("Input05")

highestSeatID = 0

for boardingPass in boardingPasses:

    # Convert input to binary
    rowData = boardingPass[:7].replace('F', '0').replace('B', '1')
    columnData = boardingPass[7:].replace('L', '0').replace('R', '1')

    # Convert binary to integer
    row = int(rowData, 2)
    column = int(columnData, 2)

    seatID = (row * 8) + column
    highestSeatID = seatID if seatID > highestSeatID else highestSeatID

print("The highest seat ID is: " + str(highestSeatID))
