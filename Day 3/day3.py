import numpy as np
import re
with open('day3input.txt', 'r') as f:
    data = f.readlines()
#data = np.array(data)
i = 0
number_arr = []
number_index = []
number_arr_copy = []
# Extracting all the numbers in an array
for line in data:
    templist = line.split(".")
    temp = list(filter(None, templist))
    te = []
    # There is an error when we have a symbol next to a number, see row data[4]
    for element in temp:
        if any(chr.isdigit() for chr in element): te.append(re.sub("[^0-9]", "", element))
        if element == '\n' or element == temp[-1]: number_arr = number_arr + te; number_arr_copy.append(te)

# Problem with reoccurring numbers in the complete number array
for line in data:
    if i == len(number_arr_copy): continue
    for number in number_arr_copy[i]:
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
    nrrr = number_arr[j] # For debugging
    last_data_row_index = len(data) - 1 # Length is 10 but last index is 9
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
            if not (first_el.isnumeric() or first_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d + 1][nr_start-1:nr_start+nr_len]:
                if not (first_el.isnumeric() or first_el == '.'):
                    part_nr_check.append('1')
        else:
            # on the top row, need to check before and after
            first_el = data[row_d][nr_start - 1]
            if not (first_el.isnumeric() or first_el == '.'):
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

    elif row_d == last_data_row_index:
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
            if not (first_el.isnumeric() or first_el == '.'):
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
            if not (first_el.isnumeric() or first_el == '.'):
                part_nr_check.append('1')
            last_el = data[row_d][nr_start + nr_len]
            if not (last_el.isnumeric() or last_el == '.'):
                part_nr_check.append('1')

            for el in data[row_d - 1][nr_start-1:nr_start+nr_len+1]:
                if not (el.isnumeric() or el == '.'):
                    part_nr_check.append('1')
            for el in data[row_d + 1][nr_start-1:nr_start + nr_len + 1]:
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

print(part_nr_list, '\nSum is: ', sum(np.array(part_nr_list,'int')))

# Getting the part-number chunk
# Storing the index of the numbers?

# Go though element by element, and make a cubical check
# Needs to handle edge numbers in a special way
# Still needs a way to check if it is a number
# Still needs a way to check if it is a symbol

# Create a truth-matrix where there are numbers, and then one for symbols
# IF it not is '.' or 'int', then we should have symbols
# If we have a number-> we have the number

# TODO: Check why part_nr_list is stacking values 285 with 286, value 173 and 383 "173*383"->"173383"