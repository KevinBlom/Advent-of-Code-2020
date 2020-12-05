from tools import *
import math
testImport()

boardingPasses = readFileToStrings("Input05")
seatIDs = []

for boardingPass in boardingPasses:

    # Convert input to binary
    rowData = boardingPass[:7].replace('F', '0').replace('B', '1')
    columnData = boardingPass[7:].replace('L', '0').replace('R', '1')

    # Convert binary to integer
    row = int(rowData, 2)
    column = int(columnData, 2)

    seatID = (row * 8) + column
    seatIDs.append(seatID)

seatIDs.sort()
walkerID = seatIDs[0]

for seatID in seatIDs:
    if seatID != walkerID:
        print(f"Your seatnumber is {walkerID}")
        walkerID += 1
    walkerID += 1
