with open('day1input.txt', 'r') as r:
    data = r.readlines()
line_nr = []
for line in data:
    number_log = []
    for char in line:
        try:
            number_log.append(int(char))
        except:
            # In the chars numbers


            pass

    last = number_log.pop(-1)
    if len(number_log) >= 1:
        first = number_log.pop(0)
    else:
        first = last

    line_nr.append(first*10+last)
print(line_nr, sum(line_nr))



