# Challenge 1
# Passports with all required fields are valid
with open('data/4.txt') as f:
  reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

  nFieldsPresent = 0
  nValidPassports = 0

  for x in f.readlines():
    if x.rstrip() == '': # Empty line
      if nFieldsPresent == len(reqFields):
        nValidPassports += 1
      nFieldsPresent = 0
      continue
    fields = [t.rstrip()[-3:] for t in x.split(':')[:-1]]
    for y in fields:
      if y in reqFields:
        nFieldsPresent += 1

  # Check last passport
  if nFieldsPresent == len(reqFields):
    nValidPassports += 1

  print(nValidPassports)

# Challenge 2
# Passports with all required fields in valid formats are valid
import re
with open('data/4.txt') as f:
  reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

  nValidFields = 0
  nValidPassports = 0
  presentFields = []

  for x in f.readlines():
    if x.rstrip() == '': # Empty line
      # Ensure that all valid fields occurred once
      if sorted(presentFields) == sorted(reqFields):
        nValidPassports += 1
      nValidFields = 0
      presentFields = []
      continue
    info = [t.rstrip() for t in x.split()]
    for y in info:
      if re.match("^byr:(19[2-9][0-9]|200[0-2])", y)\
      or re.match("^iyr:(201[0-9]|2020)$", y)\
      or re.match("^eyr:(202[0-9]|2030)$", y)\
      or re.match("^hgt:1([5-8][0-9]|9[0-3])cm$", y)\
      or re.match("^hgt:(59|6[0-9]|7[0-6])in$", y)\
      or re.match("^hcl:#[a-f0-9]{6}$", y)\
      or re.match("^ecl:(amb|blu|brn|gry|grn|hzl|oth)$", y)\
      or re.match("^pid:[0-9]{9}$", y):
        nValidFields += 1
        presentFields.append(y[:3])

  # Check last passport
  if sorted(presentFields) == sorted(reqFields):
    nValidPassports += 1

  print(nValidPassports)
