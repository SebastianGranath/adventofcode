import sys
import re
import matplotlib.pyplot as plt


def diff_array(line):
    diff_array = []
    i = 0
    current_element = line[0]

    while i != len(line)-1:
        next_element = line[i+1]


        diff = int(next_element) - int(current_element)
        if diff < 0:
            sign = diff / abs(diff)
            diff = int(abs(diff) * sign)
        diff_array.append(diff)
        i +=1
        current_element = line[i]

    return diff_array

with open('9.in', 'r') as f:
    D = f.read().strip()

data = D.split('\n')
for line in data:
    data[data.index(line)] = line.split(' ')




diff = []
end_els = []
big_calc = []
for line in data:
    line = line[::-1] # For part 2
    end_els.append(int(line[-1]))


    while diff == [] or any(diff):  # [6, 3, 0, -3, -6] gives sum =0
        diff = diff_array(line)
        if diff == []:
            end_els.append(0)
            break
        else:
            end_els.append(diff[-1])
        line = diff
    print(int(sum(end_els)))
    big_calc.append(int(sum(end_els)))
    end_els = []
    diff = []



print('answer: ', sum(big_calc))


