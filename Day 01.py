from tools import *
testImport()

lines = readFileToInts("Input01")

print(lines)

for j in range(200):
    for i in range(200):
        for x in range(200):
            if(lines[j] + lines[i] + lines[x] == 2020):
                print(lines[j] * lines[i] * lines[x])
