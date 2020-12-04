from tools import *
import re
testImport()

countOfValidPassports = 0

lines = readFileToStrings("Input04")
mandatoryProperties = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: ("cm" in x and (150 <= int(x.replace("cm", "")) <= 193)) or
                     ("in" in x and (59 <= int(x.replace("in", "")) <= 76)),
    "hcl": lambda x: re.match(r"#[0-9a-f]{6}", x) is not None,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric()
}

unprocessedPassports = []
tempPassport = []
listOfPassports = []


def evaluatePassport(passport):
  if not all(manProp in passport.keys() for manProp in mandatoryProperties.keys()):
    return 0

  for prop in passport:
    if prop in mandatoryProperties.keys() and not mandatoryProperties[prop](passport[prop]):
      return 0

  return 1


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
