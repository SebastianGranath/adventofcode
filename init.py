import os
from os import listdir
D = listdir()

high_day = 0
def next_day(high_day):
    next_day = str(int(high_day) + 1)
    new_folder = 'Day '+next_day
    os.mkdir(new_folder)

    f = open(os.path.join(new_folder, next_day + '.in'), 'w')
    #curl 'https://adventofcode.com/2023/day/' + next_day + '/input' --cookie  "session=SESSION"
    f.close()

    f = open(os.path.join(new_folder, next_day + '.test'), 'w')
    f.close()

    f = open(os.path.join(new_folder, next_day + '.py'), 'w')
    row1 = str('import sys\nimport re\n')
    row1 = row1 + str('with open(\'' + next_day + '.in\', \'r\') as f:\n')
    row1 = row1 + str('    D = f.read().strip()\n')
    f.write(row1)
    f.close()

print(listdir())

if D == []:
    next_day(high_day)
else:
    for el in D:
        el = el.split(' ')
        if el[0] == 'Day':
            high_day = el[1]
    next_day(high_day)


print(listdir())
