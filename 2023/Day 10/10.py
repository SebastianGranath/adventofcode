import sys
import re

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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


def shoelace_calculation(path):
    path.append(path[0])  # Add last element to complete loop
    path = np.array(path)

    sum = 0
    for i in range(0, len(path))[:-1]:
        el_1 = path[i]
        el_2 = path[i+1]
        calc = (el_1[0] * el_2[1]) - (el_1[1]*el_2[0])
        sum += calc
        #print('manual det', calc, 'NP det: ',np.linalg.det(path[i:i+2]))

    A = sum / 2
    b = len(path) - 1  # Remove element needed to complete the path
    # A = i + b/2 -1
    i_points = int(A + 1 - b/2)
    print('integer points:', i_points, 'Area points:', A)

    return A, i_points


with open('10.in', 'r') as f:
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

path_A = []
path_B = []

while n_coord[0] != n_coord[1]:
     # logic to take path not traveled
    path += n_coord
    path_A += [n_coord[0]]
    path_B += [n_coord[1]]
    for i in range(len(n_coord)):
        # Select one of the coords.
        n_coord[i], old_coord[i] = follow_letters(n_coord[i], old_coord[i], D)
        if len(n_coord) != 2:
            raise ValueError
    steps += 1
    #print('Change: ', n_coord, old_coord, ' at step: ', steps)

if n_coord[0] == n_coord[1]:
    path.append(n_coord[0])
    path_A = [(r, c)] + path_A
    path_B = path_B + [n_coord[0]]
    sorted_path = path_A+path_B[::-1]  # Flip B-array to get circle

area, i_points = shoelace_calculation(sorted_path[::-1])

path_matrix = np.zeros([len(D), len(D[0])])

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(path_matrix, cmap='Greys', origin='lower')

# Initialize the line plot
line, = ax.plot([], [], color='blue', linewidth=1)

# Initialize the red dot for the current position
current_dot, = ax.plot([], [], color='red', marker='o', markersize=5, linestyle='None')


# Initialize the path data
def init():
    line.set_data([], [])
    current_dot.set_data([], [])
    return im, line, current_dot,

# Update the path for the animation
def update(frame):
    # Extract x and y coordinates up to the current frame
    path_x, path_y = zip(*sorted_path[:frame + 1])

    # Update the line
    line.set_data(path_y, path_x)

    # Update the current dot (most recent point)
    current_dot.set_data([path_y[-1]], [path_x[-1]])

    return im, line, current_dot,


# Create the animation
ani = FuncAnimation(fig, update, frames=range(0,len(sorted_path), 3), init_func=init, blit=True, repeat=False,  interval=0.01)

plt.title('Movement Path Animation, i-points: '+ str(i_points) + ', Area: ' + str(area))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')


# After the animation, fill the enclosed area
def fill_area_after_animation(*args):
    # Extract x and y coordinates of the full path
    path_x, path_y = zip(*sorted_path)

    # Fill the area inside the path
    ax.fill(path_y, path_x, color='yellow', alpha=0.4)  # Adjust alpha for transparency

    plt.draw()  # Redraw the plot with the filled area



# Connect the fill function to be called after the animation ends
ani.event_source.stop = fill_area_after_animation


plt.show()