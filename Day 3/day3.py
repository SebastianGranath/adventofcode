import numpy as np
with open('day3input.txt', 'r') as f:
    data = f.readlines()
#data = np.array(data)
i = 0; j = 0
for line in data:
    for char in line:
        if not char == '.' and not char.isnumeric():
            if char == '\n': print('linebreak')
            print('Symbol: ', char)
        j = j + 1
    i = i + 1
print(i,j)

# Getting the part-number chunk

# Go though element by element, and make a cubical check
# Needs to handle edge numbers in a special way
# Still needs a way to check if it is a number
# Still needs a way to check if it is a symbol

# Create a truth-matrix where there are numbers, and then one for symbols
# IF it not is '.' or 'int', then we should have symbols
# If we have a number-> we have the number