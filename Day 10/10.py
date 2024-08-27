import sys
import re

import numpy as np


def get_adjacent_chars(r,c, D):
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

    illegal_moves = {
        'left': {'|', 'J', '7'},
        'up': {'L', 'J', '-'},
        'right': {'|', 'L', 'F'},
        'down': {'7', 'F', '-'}
    }

    i = 0
    for direction, move in zip(directions, moves):
        char = adj_steps.get(direction)
        if char is None or char == '.':
            continue
        if char in illegal_moves[direction]:
            continue

        # Update the new coordinates based on the move and direction
        new_coordinates[i] = tuple(a + b for a, b in zip(old_coordinates[i], move))
        i += 1

    return new_coordinates, old_coordinates

def follow_letters(coordinate, old_coordinate, D):
    direction = tuple(a - b for a, b in zip(coordinate, old_coordinate))
    letter = D[coordinate[0]][coordinate[1]]

    movement_map = {
        '|': {(-1, 0): (-1, 0), (1, 0): (1, 0)},
        '-': {(0, 1): (0, 1), (0, -1): (0, -1)},
        'L': {(1, 0): (0, 1), (0, -1): (-1, 0)},
        'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
        '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
        'F': {(-1, 0): (0, 1), (0, -1): (1, 0)},
    }

    updated_coordinates = tuple(a + b for a, b in zip(coordinate, movement_map[letter][direction]))
    return updated_coordinates, coordinate


def sholace_calculation(path):
    path = np.array(path)
    sum = 0
    for i in range(0, len(path))[:-1]:
        el_1 = path[i]
        el_2 = path[i+1]
        sum += np.linalg.det(path[i:i+2])
        print(np.linalg.det(path[i:i+2]))

    A = sum/2
    b = len(path)
    # A = i + b/2 -1
    i_points = A + 1 - b/2
    print('integer points:', i_points, 'Area points:', A)

    return sum/2



def calculate_enclosed_area(path, D):
    area = 0

    for r, row in enumerate(D):
        counter = 0
        stop = 0
        i = 0
        for c, column in enumerate(row):
            if (r, c) in path and (r+1, c+1 not in path):
                # If current element is in path, but not the next
                i = 0
                counter += 1
                while not stop:
                    if (r, c) in path:
                        # Once an element if found, calculate area, and return new value for current c
                        area += i
                        stop = 1
                    i += 1


        print('Row: ',r, ' has ', counter, ' elements. Area: ', area)

                # if not (r, c + 1) in path and c + 1 != len(row) - 1:
                #     while not (r, c_copy) in path:
                #         area += 1
                #         c_copy += 1
                #     c = c_copy


    return area



with open('10.test', 'r') as f:
    D = f.read().strip()

D =D.split('\n')
path = []
for row in D:
    for char in row:
        if char == 'S':
            c = row.index(char)
            r = D.index(row)
            continue

adj_c = get_adjacent_chars(r, c, D)

path.append((r, c))

n_coord, old_coord = take_first_step(r, c, adj_c)
steps = 1
while n_coord[0] != n_coord[1]:
     # logic to take path not traveled
    path += n_coord

    for i in range(len(n_coord)):
        # Select one of the coords.
        n_coord[i], old_coord[i] = follow_letters(n_coord[i], old_coord[i], D)
        if len(n_coord) != 2:
            raise ValueError
    steps += 1
    print('Change: ', n_coord, old_coord, ' at step: ', steps)

if n_coord[0] == n_coord[1]:
    path.append(n_coord[0])
area = calculate_enclosed_area(path, D)

sholace_calculation([(3,0),(0,1),(1,2),(2,3),(3,4),(4,4),(5,4),(2,4),(3,0)])
#area = sholace_calculation(path)
interior = 0
path_matrix = np.zeros([len(D), len(D[0])])
for p in path:
    r,c = p
    path_matrix[r][c] = 1