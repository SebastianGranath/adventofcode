import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('5.in', 'r') as f:
    rules, D = f.read().strip().split('\n\n')
D = D.strip().split()
rules = rules.strip().split()
print(f"rules:{rules}\nD: {D}")

def applyRules(row, rules):

    #print(row, rules)
    for index, el in enumerate(row):
        
        # Here i should store what rules to check for each number in a global varible
        # Points to an index
        firstCheck = [i for i, item in enumerate(rules) if item.startswith(f"{el}|")]

        for i in firstCheck:
            controled_element = rules[i].split('|')[1]
            if controled_element not in row:
                continue
            if row.index(controled_element) < index:
                print(f'error: rule broken for {el} is not before {controled_element}')
                return False
            else:
                continue

        secondCheck = [i for i, item in enumerate(rules) if item.endswith(f"|{el}")]

        #print(secondCheck)
        for i in secondCheck:
            controled_element2 = rules[i].split('|')[1]
            if controled_element2 not in row:
                continue
            if row.index(controled_element2) > index:
                print(f'error: rule broken for {el} is not after {controled_element2}')
                return False
            else:
                continue
   
    return int(row[(len(row)//2)])


def applyRules2(row, rules):

    #print(row, rules)
    for _ in range(10):
        for index, el in enumerate(row):
            
            # Here i should store what rules to check for each number in a global varible
            # Points to an index
            firstCheck = [i for i, item in enumerate(rules) if item.startswith(f"{el}|")]

            for i in firstCheck:
                controled_element = rules[i].split('|')[1]
                if controled_element not in row:
                    continue
                if row.index(controled_element) < index:
                    #print(f'switching: element {el} with {controled_element}')
                    
                    # Switch elements, tested and ok
                    tmp1 = row[index]
                    row[index] = controled_element
                    row[row.index(controled_element)] = tmp1


            secondCheck = [i for i, item in enumerate(rules) if item.endswith(f"|{el}")]

            #print(secondCheck)
            for i in secondCheck:
                controled_element2 = rules[i].split('|')[1]
                if controled_element2 not in row:
                    continue
                if row.index(controled_element2) > index:

                    #print(f'switching: element {el} with {controled_element}')
                    

                    tmp1 = row[index]
                    row[index] = controled_element2
                    row[row.index(controled_element2)] = tmp1
                    return False
                else:
                    continue
    
   # print(f"row at end of check2: {row}")
    return int(row[(len(row)//2)])


def checkInput(D, rules):
    correctSum = 0
    count = 0
    incorrectRows = []
    for idx, row in enumerate(D):
        row = row.split(',')
        print(f'controlling row {idx}...')
        validRow = applyRules(row, rules)
        if validRow:
            print(f'controlling row {idx}: passed')
            correctSum += 1
            count += int(validRow)
            print(validRow)
        else:
            incorrectRows.append(idx)
    return correctSum, count, incorrectRows

def checkInput2(D, rules):
    correctSum = 0
    count = 0
    for idx, row in enumerate(D):
        row = row.split(',')
        print(f'controlling row {idx}...')
        validRow = applyRules2(row, rules)
        if validRow:
            print(f'controlling row {idx}: passed')
            correctSum += 1
            count += int(validRow)
            print(validRow)
    return correctSum, count

correctSum, count, inccorectRows = checkInput(D, rules)
#print(f"inccorectRows: {inccorectRows}\nD: {D}")

newD = [D[i] for i in inccorectRows]
print(newD)

correctSum2, count2 = checkInput2(newD, rules)
print(f"Part 1: correct sum: {count}")
print(f"Part 2: correct sum: {count2}") # 232 too low, 6123 too low, 6377 too high
