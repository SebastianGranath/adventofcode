import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('4.in', 'r') as f:
    D = f.read().strip()



# Text search vertical
count = 0 
pattern1 = r"XMAS"
pattern2 = r"SAMX"
res1 = re.findall(pattern1, D)
res2 = re.findall(pattern2, D)
count += (len(res1)+len(res2))



def take_step(i,j):
    up =    [[-1, -1], [-1, 0], [-1, 1]]
    down =  [[1, -1], [1, 0], [1, 1]]
    counter = 0

    for pair in up:
        for ii in range(3):
            row = j+  pair[1]*ii
            col = i +  pair[0]*ii
            try:
                print(f'index: {row},{col}')
                if ii == 1 and D[row][col] != 'M': break
                if ii == 2 and D[row][col] != 'A': break
                if ii == 3 and D[row][col] != 'S': 
                    counter += 1
            except IndexError:
                print('out of bounds')
                break

    for pair in down:
        for ii in range(3):
            row = j+  pair[1]*ii
            col = i + pair[0]*ii
            try:
                print(f'index: {row},{col}')
                if ii == 1 and D[row][col] != 'M': break
                if ii == 2 and D[row][col] != 'A': break
                if ii == 3 and D[row][col] != 'S': 
                    counter += 1
            except IndexError:
                print('out of bounds')
                break

    return counter

# Find the vertical
score = 0
D = D.splitlines()
for i, row in enumerate(D):
    for j, el in enumerate(row):
        if el == 'X':
            score += take_step(i,j)
            print(score)
            input()

            top_limit += 1


print(f'counter: {count}, score: {score}, ---> result: {score+count}')
            
            
