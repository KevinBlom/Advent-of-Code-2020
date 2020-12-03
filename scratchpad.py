# Day 2: Password Philosophy --- Puzzle Input ---

file = open('Inputs/input02.txt')

passwords = []
for line in file:
    passwords.append(line.rstrip())

# Create an array of requirements and passwords
for i in range(len(passwords)):
    new_value = passwords[i].replace('-', ' ')
    new_value = new_value.replace(':', '')
    new_value = new_value.split(' ')
    new_value[0] = int(new_value[0])
    new_value[1] = int(new_value[1])
    passwords[i] = new_value

# Day 2: Password Philosophy --- Part 1 ---

# Some values for stuff
passlist = passwords
correct_passes = 0

# Counting all valid passwords
for i in passlist:
    if (i[3].count(i[2]) >= i[0]) and (i[3].count(i[2]) <= i[1]):
        correct_passes += 1

# Print a thing
print('A total of', correct_passes,
      'was correct, out of a possible', len(passlist))

# Day 2: Password Philosophy --- Part 2 ---

# Some values for stuff
passlist = passwords
correct_passes = 0

# Counting all valid passwords
for i in passlist:
    if (i[3][i[0] - 1] == i[2]) ^ (i[3][i[1] - 1] == i[2]):
        correct_passes += 1

# Print a thing
print('A total of', correct_passes,
      'was correct, out of a possible', len(passlist))
