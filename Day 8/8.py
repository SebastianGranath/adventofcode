import sys; import re
import math
from functools import reduce


def node2dict(nodes):
    # Define a regex pattern to extract the key-value pairs
    pattern = r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)"
    matches = re.findall(pattern, nodes)  # Use re.findall to extract all matches
    relationship_dict = {key: (value1, value2) for key, value1, value2 in matches}
    return relationship_dict

def path(start, goal, nodes, instructions):
    idx = 0
    steps = 0
    current_node = start
    path = [start]
    while current_node != goal:
        for i in range(len(instructions)):
            letter = instructions[i]
            if letter == 'L':
                idx = 0
            else:  # Letter == 'R'
                idx= 1
            next_node = nodes[current_node][idx]
            path.append(next_node)
            current_node = next_node
            steps += 1
    return steps

def paths(starts, goals, nodes, instructions):
    pattern = re.compile(r'Z$')

    idx = 0
    steps = 0
    current_nodes = starts

    path = [start_node]
    while sorted(current_nodes) != sorted(goals):
        for i in range(len(instructions)):
            if pattern.search(current_nodes) != None:
                return steps
            letter = instructions[i]
            if letter == 'L':
                idx = 0
            else:  # Letter == 'R'
                idx= 1
            next_nodes = nodes[current_nodes][idx]
            path.append(next_nodes)
            current_nodes = next_nodes
            steps += 1
            if steps % 1000000 == 0:
                print(steps)
                print(current_nodes)
    return steps

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

with open('8.in', 'r') as f:
    D = f.read().strip()
instructions, nodes = D.split('\n\n')


nodes = node2dict(nodes)
# Part 1
start_node ='AAA'
goal_node = 'ZZZ'
steps = path(start_node, goal_node, nodes, instructions)
print('Steps in part 1: ', steps)

# Part 2
pattern = re.compile(r'\b\w*A\b')
start_nodes = [key for key in nodes.keys() if pattern.search(key)]

pattern = re.compile(r'\b\w*Z\b')
end_nodes = [key for key in nodes.keys() if pattern.search(key)]
steps2 = []
for i in range(len(start_nodes)):
    steps2.append(paths(start_nodes[i], end_nodes[0], nodes, instructions))
print('Steps in part 2: ', steps2)
result = lcm_multiple(steps2)

print(result)

