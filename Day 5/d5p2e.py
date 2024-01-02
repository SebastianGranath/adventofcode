import sys
import re

from collections import defaultdict

with open('d5input.txt', 'r') as f:
    D = f.read()

L = D.split('\n')
p1 = 0

parts = D.split('\n\n')
seed, *others = parts
seed = seed.split(':')[1].split()

def f(x, o):
    for line in o:
        d,s,r = [int(x) for x in line.split()]
        if s<=x<s+r:
            return d+(x-s)
        return x

S = []
for s in seed:
    s = int(s)
    for o in others:
        O = o.split('\n')
        s = f(s, O[1:])
    S.append(s)
print(min(S))