from tools import *
testImport()

bagsInput = readFileToStrings("Input07")
bags = {}


def findBagColor(bag):
    return bag[:bag.index('bags')].strip()


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
        if subBag == 'other':
            return False
        elif subBag == 'shiny gold':
            return True
        else:
            if canContainShinyGoldBag(subBag):
                return True


for bag in bagsInput:
    bag = bag.strip('\n')
    bag = bag.strip('.')
    bagColor = findBagColor(bag)
    bags[bagColor] = findContentsOfBag(bag)


shinyGoldCounter = 0
for bag in bags.keys():
    print('Starting search from dict:' + bag)
    if canContainShinyGoldBag(bag):
        shinyGoldCounter += 1

print(shinyGoldCounter)
