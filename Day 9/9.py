import sys
import re



def diff_array(line):
    for num in line: line[line.index(num)] = int(num)

    diff_array = []
    i = 0
    current_element = line[0]
    while current_element != line[-1]:
        next_element = line[i+1]

        diff = next_element - current_element
        diff_array.append(diff)
        i +=1
        current_element = line[i]
    if current_element == line[-1]:
        for _ in line: diff_array.append(0)
        return diff_array
    return diff_array

with open('9.test', 'r') as f:
    D = f.read().strip()

data = D.split('\n')
for line in data:
    data[data.index(line)] = line.split(' ')

diff = []
for line in data:
    end_els = []
    while sum(diff) != 0 or diff == []:
        diff = diff_array(line)
        end_els.append(diff[-1])
        line = diff
    print(end_els)


