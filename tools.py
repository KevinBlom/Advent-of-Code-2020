def testImport():
    print("Import of tools succeeded!")


def readFileToInts(name) -> list:
    file = open("Inputs/" + name + ".txt")
    lines = list(map(int, file.readlines()))
    print("Loaded " + str(len(lines)) + " lines of data.")
    return lines


def readFileToStrings(name):
    file = open("Inputs/" + name + ".txt")
    lines = list(map(str, file.readlines()))
    print("Loaded " + str(len(lines)) + " lines of data.")
    return lines


def printLines(list):
    for line in list:
        print(line)
