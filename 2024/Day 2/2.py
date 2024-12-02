import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('2.in', 'r') as f:
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
    #print('passed row: ', row)
    return sum

def checkSafe2(row):
    def verifyList(lst):
        oldSign = 0
        for index, value in enumerate(lst):
            if index == 0:  # Skip the first element
                continue

            step = lst[index] - lst[index - 1]  # Calculate the step
            if step == 0:  # Consecutive numbers are the same, fail
                print(f"x--- at {index}: {lst}")
                return 0, index
            
            sign = -1 if step < 0 else 1  # Determine the direction (sign)
            abs_step = abs(step)

            # Validate the step size and direction
            if 1 <= abs_step <= 3 and (oldSign == 0 or oldSign == sign):
                oldSign = sign
                continue
            else:  # Step is invalid
                print(f"x--- at {index}: {lst}")
                return 0, index
        print(f"0--- at {index}: {lst}")
        return 1, index  # All elements are valid

    # Parse the row into integers
    row = list(map(int, row.split()))

    # Attempt to verify the list as-is
    res, index = verifyList(row)

    if res == 1:
        return 1  # Sequence is valid
    else:
        # Remove the problematic element and re-check
        res1, _ = verifyList(row[:index] + row[index + 1:])
        if res1 == 1:
            return 1
        else:
            for i in range(len(row)):
                res, _ = verifyList(row[:i]+row[i+1:])
                if res == 1:
                    return 1

              # Sequence is valid after removing the element
    return 0  # Sequence is invalid

p1_approvals = 0
p2_approvals = 0
p2_fails = 0
var = 0
for line in D:
    p1_approvals += checkSafe(line)
    var = checkSafe2(line)
    if var == 0:
        p2_fails +=1
    else:
        p2_approvals += var
print('part1: ',p1_approvals, '\npart2: ', p2_approvals, '\np2_fails', p2_fails)

# Fails, 461
    
        
# All increasing, or all decreasing
# each step, min 1 max 3

