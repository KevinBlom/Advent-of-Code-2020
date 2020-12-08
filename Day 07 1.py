from tools import *
testImport()

bagsInput = readFileToStrings("Input07")

bags = {}


def findBagColor(bag):
    return bag[:bag.index('bags')].strip()
    pass


def findContentsOfBag(bag):
    tempString = bag.partition('bags contain ')[2]
    tempString = tempString.split(',')
    tempString = list(map(lambda x: x[2:], tempString))
    tempString = list(map(lambda x: x.replace('bags', ''), tempString))
    tempString = list(map(lambda x: x.replace('bag', ''), tempString))
    tempString = list(map(lambda x: x.strip(), tempString))
    return tempString


def canContainShinyGoldBag(bag):
    for subBag in bags[bag]:
        print('Searching in: ' + subBag)
        if subBag == 'other':
            return False
        elif subBag == 'shiny gold':
            print('Found shiny!')
            return True
        else:
            return canContainShinyGoldBag(subBag)


for bag in bagsInput:
    bag = bag.strip('\n')
    bag = bag.strip('.')
    bagColor = findBagColor(bag)
    bags[bagColor] = findContentsOfBag(bag)

shinyGoldCounter = 0
for bag in bags.keys():
    if canContainShinyGoldBag(bag):
        shinyGoldCounter += 1


print(shinyGoldCounter)
