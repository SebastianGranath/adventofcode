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

def ray_search(i, j, D):
    # This algorithm skips the vertical searches that regex handled for us.

    ray_limit = 3  # corresponds to length limit of ray  (x) m a s -> 3
    # conditions
    h_moves = []
    if i >= ray_limit: h_moves.append([-1, 0])  # add move up
    if i < len(D) - ray_limit : h_moves.append([1, 0])  # add move down

    v_moves = []
    if j >= ray_limit: v_moves.append([0, -1])  # add move left
    if j < len(D[0]) - ray_limit : v_moves.append([0, 1])  # add move right

    vertical_moves = []
    if i >= ray_limit: 
        vertical_moves.append([-1, 0])  # straight vertical up
    if i < len(D) - ray_limit: 
        vertical_moves.append([1, 0])  # straight vertical down

    score = 0
    for H in h_moves:
        for V in v_moves:
            #print(f"start: ({i},{j}) H_move: {H}, V_move: {V}")
            ii = i
            jj = j
            for step in range(ray_limit):
                #print(f"i,j: {ii,jj}, new index: ({ii + (1 + step) * H[0],jj + (1 + step)*V[1]})")
                if step == 0 and D[ ii + (1 + step) * H[0]][jj + (1 + step)*V[1]] != 'M': 
                    #print('0 failed at M')
                    break
                if step == 1 and D[ ii + (1 + step) * H[0]][jj + (1 + step)*V[1]] != 'A': 
                    #print('0 failed at A')
                    break
                if step == 2 and D[ ii + (1 + step) * H[0]][jj + (1 + step)*V[1]] == 'S': 
                    score += 1 
                    #print('-->Success!!')
                elif step == 2:
                    #print('0 failed at S')
                    pass
    
     # Process vertical moves
    for V in vertical_moves:
        ii = i
        for step in range(ray_limit):
            if step == 0 and D[ii + (1 + step) * V[0]][j] != 'M': 
                break
            if step == 1 and D[ii + (1 + step) * V[0]][j] != 'A': 
                break
            if step == 2 and D[ii + (1 + step) * V[0]][j] == 'S': 
                score += 1 
    return score


def ray_search2(i, j, D):
    # This algorithm skips the vertical searches that regex handled for us.

    ray_limit = 1  # corresponds to length limit of ray  (x) m a s -> 3

    score = 0
    # conditions
    h_moves = []
    if i >= ray_limit: h_moves.append([-1, 0])  # add move up
    if i < len(D) - ray_limit : h_moves.append([1, 0])  # add move down

    v_moves = []
    if j >= ray_limit: v_moves.append([0, -1])  # add move left
    if j < len(D[0]) - ray_limit : v_moves.append([0, 1])  # add move right

    if [-1,0] in h_moves and [1,0] in h_moves:
        if [0,-1] in v_moves and [0,1] in v_moves:
            if ( ((D[i-1][j-1] == 'M' and D[i+1][j+1] == 'S') or (D[i-1][j-1] == 'S' and D[i+1][j+1] == 'M')) 
                    and ((D[i-1][j+1] == 'M' and D[i+1][j-1] == 'S') or (D[i-1][j+1] == 'S' and D[i+1][j-1] == 'M')) ):
                print(f'passed: {i,j}')
                score += 1
    return score

# Find the starting points (X)
score = 0
score2 = 0
D = D.splitlines()
for i, row in enumerate(D):
    for j, el in enumerate(row):
        if el == 'X':
            # score += take_step(i,j)
            score += ray_search(i ,j ,D)

for i, row in enumerate(D):
    for j, el in enumerate(row):
        if el == 'A':
            score2 += ray_search2(i, j, D)




print(f'\nPart 1: Horizontal counter: {count}, score: {score}, ---> result: {score+count}')
print(f'Part 2: X-MAS counter: {score2} ---> result: {score2}')
            
            
