from tools import *
testImport()

countOfValidPassports = 0

lines = readFileToStrings("Input04")
mandatoryProperties = ['byr',
                       'iyr',
                       'eyr',
                       'hgt',
                       'hcl',
                       'ecl',
                       'pid', ]
optionalProperties = ['cid']

unprocessedPassports = []
tempPassport = []
listOfPassports = []


def evaluatePassport(passport):
  if all(manProps in passport for manProps in mandatoryProperties):
    return 1
  else:
    return 0


for line in lines:
  if line != "\n":
    properties = line.split()
    for element in properties:
      tempPassport.append(element)
  else:
    unprocessedPassports.append(tempPassport)
    tempPassport = []


for passport in unprocessedPassports:
  listOfPassports.append(dict(e.split(':') for e in passport))

for passport in listOfPassports:
  countOfValidPassports += evaluatePassport(passport)

print(countOfValidPassports)
