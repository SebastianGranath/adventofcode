import sys
import re

import numpy as np


def next_step(r,c, D):
    # Left Up Right Down
    moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    directions = ['left', 'up', 'right', 'down']

    nr_rows = len(D)
    nr_columns = len(D[0])
    adjecent_chars = {}

    for i, (dr, dc) in enumerate(moves):
        new_r = r + dr
        new_c = c + dc

        if 0 <= new_r <= nr_rows and 0 <= new_c <= nr_columns:
            adjecent_chars[directions[i]] = D[new_r][new_c]
        else:
            adjecent_chars[directions[i]] = None
    return adjecent_chars

def take_first_step(r ,c, adj_steps):
    # Takes start coordinate, and return coordinates of
    old_coordinates = [(r,c),(r,c)]
    new_coordinates = [(-1,-1),(-1,-1)]

    moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    directions = ['left', 'up', 'right', 'down']

    i = 0
    for step in adj_steps:

        # Need logic here for illegal moves, e.g. cannot move left to a |
        if adj_steps[step] == '.' or adj_steps[step] == None:
            continue
        else:
            new_coordinates[i] = tuple(a + b for a, b in zip(old_coordinates[i], moves[directions.index(step)]))
            i += 1
    return new_coordinates, old_coordinates

def follow_letters(coordinate, old_coordinates, D):
    # Get two set of coordinates, return their next step
    # in --> [(2,1),(3,0)]
    # Get letters for each coordinate (Row, Column)
    # left (0 , -1) up (1, 0) right (0, 1) down  (-1, 0)



    direction = tuple(a - b for a, b in zip(coordinate, old_coordinates))
    letter = D[coordinate[0]][coordinate[1]]
    if letter == '|':
        # Check: Handle both directions
        if direction == (-1, 0):
            # Go up
            updated_coordinates = tuple(a + b for a, b in zip(coordinate, (-1, 0)))
        else:
            # Go down
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (1, 0)))

    elif letter =='-':
        # Check: Handle both directions
        if direction == (0, 1):
            # Go right
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (0, 1)))
        else:
            # Go left
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (0, -1)))

    elif letter == 'L':
        if direction == (1, 0):
            # Go right
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (0, 1)))
        else:
            # Go up
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (-1, 0)))
    elif letter == 'J':
        if direction == (0, 1):
            # Go up
            updated_coordinates = tuple(a + b for a, b in zip(coordinate, (-1, 0)))
        else:
            # Go left
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (0, -1)))
    elif letter == '7':
        if direction == (0, 1):
            # Go down
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (1, 0)))
        else:
            # Go left
            updated_coordinates=tuple(a + b for a, b in zip(coordinate, (0, -1)))
    elif letter == 'F':
        if direction == (-1, 0):
            # Go right
            updated_coordinates = tuple(a + b for a, b in zip(coordinate, (0, 1)))
        else:
            # Go down
            updated_coordinates = tuple(a + b for a, b in zip(coordinate, (1, 0)))

    return updated_coordinates, coordinate

with open('10.in', 'r') as f:
    D = f.read().strip()

D =D.split('\n')

for row in D:
    for char in row:
        if char == 'S':
            c = row.index(char)
            r = D.index(row)
            continue

adj_c = next_step(r, c, D)

n_coord, old_coord = take_first_step(r, c, adj_c)
print(n_coord, old_coord)
steps = 1
while n_coord[0] != n_coord[1]:
     # logic to take path not traveled

    for i in range(len(n_coord)):
        #r, c = n_coord[i], old_coord [i]
        #adj_c = next_step(r, c, D)
        # Select one of the coords.
        n_coord[i], old_coord[i] = follow_letters(n_coord[i], old_coord[i], D)
        if len(n_coord) != 2:
            raise ValueError
    steps += 1
    print('Change: ', n_coord, old_coord, ' at step: ', steps)
print(steps)

