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
        if adj_steps[step] == '.' or adj_steps[step] == None:
            continue
        else:
            new_coordinates[i] = tuple(a + b for a, b in zip(old_coordinates[i], moves[directions.index(step)]))
            i += 1
    return new_coordinates, old_coordinates

def follow_letters(new_coordinates, old_coordinates, D):
    # Get two set of coordinates, return their next step
    # in --> [(2,1),(3,0)]
    # Get letters for each coordinate
    updated_coordinates = []
    for coordinate, old_coord in zip(new_coordinates,old_coordinates):
        direction = tuple(a - b for a, b in zip(coordinate, old_coord))
        letter = D[coordinate[0]][coordinate[1]]
        if letter == '|':
            # Check: Handle both directions
            updated_coordinates.append( tuple(a + b for a, b in zip(new_coordinates, direction)) )
        elif letter =='-':
            # Check: Handle both directions
            updated_coordinates.append( tuple(a + b for a, b in zip(coordinate, direction)) )
        elif letter == 'L':
            pass
        elif letter == 'J':
            pass
        elif letter == '7':
            pass
        elif letter == 'F':
            pass
    # get new coordinate, and return

    return new_coordinates

with open('10.test', 'r') as f:
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
while n_coord[0] != n_coord[1]:
    for coord in n_coord:
        r, c = coord
        adj_c = next_step(r, c, D)
        n_coord, old_coord = follow_letters(n_coord, old_coord, D)

