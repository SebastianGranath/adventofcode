import sys
import re, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(r"1.in", 'r') as f:
    D = f.read().strip().splitlines()

list1, list2 = map(list, zip(*[map(int, line.split()) for line in D]))

def distanceCalculator(list1, list2):
    num1 = list1.pop(list1.index(min(list1)))
    num2 = list2.pop(list2.index(min(list2)))
    distance = abs(num1-num2)
    return list1, list2, distance

def similarityScoreCalulator(list1, list2):
    similarityScore = 0
    for el in list1:
        similarityScore += el*list2.count(el)
    print('SimilarityScore: ', similarityScore)
## Part 1
## ------
# dist = 0
# while list1 and list2 != []:
#     list1, list2, distance = distanceCalculator(list1, list2)
#     dist += distance
# print('Distance: ',dist)

## Part 2
## ------
similarityScoreCalulator(list1, list2)
