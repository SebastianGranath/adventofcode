import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('2.test', 'r') as f:
    D = f.read().strip().splitlines()
print(D)



def checkSafe(row):
    sum = 1
    row = row.split()
    start = int(row.pop(0))
    if int(row[0]) == start:
        return 0
    oldSign = (int(row[0])-start)/abs(int(row[0])-start)

    for el in row:

        step = int(el) - start
        if step == 0:
            return 0
        sign = step / abs(step)

        if abs(step)<4 and abs(step)>0 and sign == oldSign:
            pass
        else:
            return 0
        oldSign = sign
        start = int(el)
    print('passed row: ', row)
    return sum

def checkSafe2(row):
    rowCopy  = str(row)
    row = row.split()
    row.pop(0)
    print(rowCopy, row)
    return 0
    # If error element is removed, the new array should work

p1_approvals = 0
p2_approvals = 0

for line in D:
    #p1_approvals += checkSafe(line)
    p2_approvals += checkSafe2(line)
print('part1: ',p1_approvals, '\npart2: ', p2_approvals)
    
        
# All increasing, or all decreasing
# each step, min 1 max 3

