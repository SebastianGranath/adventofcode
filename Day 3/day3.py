import numpy as np
with open('day3input.txt', 'r') as f:
    data = f.readlines()
#data = np.array(data)
i = 0
number_arr = []
number_index =[]
# Extracting all the numbers in an array
for line in data:
    temp = line.split(".")
    # There is an error when we have a symbol next to a number, see row data[4]
    for element in temp:
        if any(chr.isdigit() for chr in element): number_arr.append(element)


for line in data:
    for number in number_arr:
        try:
            number_index.append([i, line.index(number), len(number)])
        except:
            pass
    i = i + 1

j = 0
part_nr_check = []
part_nr_list = []
for number in number_index:
    row_d = number[0]
    nr_start = number[1]
    nr_len = number[2]
    if row_d == 0:
        # Scenario when we are at the top row, only need to check element be4 n after nr plus row below
        if nr_start == 0:
            # Top row, skip first element
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')
            for el in data[row_d + 1][nr_start:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')

        elif nr_start + nr_len == len(data[row_d]):
            # Top row, skip last element
            first_el = data[row_d][nr_start - 1]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d + 1][nr_start-1:nr_start+nr_len]:
                if not (last_el.isnumeric() or last_el == '.'):
                    part_nr_check.append('1')
        else:
            # on the top row, need to check before and after
            first_el = data[row_d][nr_start - 1]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d + 1][nr_start-1:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')

        if any(part_nr_check) == 1:
            part_nr_list.append(number_arr[j])
            part_nr_check = []

    elif row_d == len(data):
        if nr_start == 0:
        # Last row, only need to check current row and row above
            # Top row, skip first element
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')
            for el in data[row_d - 1][nr_start:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')

        elif nr_start + nr_len == len(data[row_d]):
            # bottom row, skip last element
            first_el = data[row_d][nr_start - 1]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d - 1][nr_start-1:nr_start+nr_len]:
                if not (last_el.isnumeric() or last_el == '.'):
                    part_nr_check.append('1')
        else:
            # on the bottom row, need to check before and after
            first_el = data[row_d][nr_start - 1]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d - 1][nr_start-1:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')

        if any(part_nr_check) == 1:
            part_nr_list.append(number_arr[j])
            part_nr_check = []

    else:
        # In the middle, need to check current row, row above, row below
        if nr_start == 0:
            # middle row, skip first element
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')
            for el in data[row_d - 1][nr_start:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')
            for el in data[row_d + 1][nr_start:nr_start + nr_len + 1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')

        elif nr_start + nr_len == len(data[row_d]):
            # middle row, skip last element
            first_el = data[row_d][nr_start - 1]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d - 1][nr_start-1:nr_start+nr_len]:
                if not (last_el.isnumeric() or last_el == '.'):
                    part_nr_check.append('1')

            for el in data[row_d + 1][nr_start:nr_start + nr_len + 1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')
        else:
            # middle row, need to check before and after
            first_el = data[row_d][nr_start - 1]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d - 1][nr_start-1:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')
            for el in data[row_d + 1][nr_start:nr_start + nr_len + 1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')

        if any(part_nr_check) == 1:
            part_nr_list.append(number_arr[j])
            part_nr_check = []
    j = j + 1



    #elif number[0] == len(data):
        # Scenario when we are at the bottom row
    #else:
        # Scenario when we are in the middle


    pass
    # Number = [x, x, x]
    # number[0] - line in Data where number is located
    # number[1] - the index of where the number starts
    # number[2] - how long the number is
    # number[0]-1: row above number
    # number[0]+1: row below number
    # How to handle 0
    # data[number[0]][number[1]-1:number[1]+number[2]]: The horizontal scan



# Cubial check?
# for number in number_arr:
# data.index(number)
'''
    for char in line:

        if not char == '.' and not char.isnumeric():
            if char == '\n': pass #print('linebreak')
            pass
            #print('Symbol: ', char)
        j = j + 1
    i = i + 1
'''
print(data)
print(number_arr)
print(number_index)

# Getting the part-number chunk
# Storing the index of the numbers?

# Go though element by element, and make a cubical check
# Needs to handle edge numbers in a special way
# Still needs a way to check if it is a number
# Still needs a way to check if it is a symbol

# Create a truth-matrix where there are numbers, and then one for symbols
# IF it not is '.' or 'int', then we should have symbols
# If we have a number-> we have the number