from tools import *
testImport()

directions = readFileToStrings("Input12")

actions = {
    'N' : lambda x: x[2] + x,
}

shipState = [0, 0, 0] # 0 E/W, 0 N/S, 0 degrees = pointing east

