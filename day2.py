import pandas as pd

test_input = pd.read_csv("day2_input.csv", delim_whitespace=True, header=None)
#col 0 is min-max, col 1 is the letter, col 2 is the password
print(test_input.iloc[0,2])

total = len(test_input)
print(total)
#part1

validpass_part1 = 0
validpass_part2 = 0

for i in range(total):
    password = test_input.iloc[i,2]
    limit = test_input.iloc[i,0].split('-')
    limit = [int(x) for x in limit] #0 min 1 max
    position = limit

    letter = test_input.iloc[i,1].replace(':','')

    counter = password.count(letter) #min<counter<max

    if counter>= limit[0] and counter<=limit[1]:
        validpass_part1+=1

    if letter == password[position[0]-1] or letter == password[position[1]-1]:
        if password[position[0]-1] != password[position[1]-1]:
            print(letter, password[position[0]-1], password[position[1]-1])
            validpass_part2+=1

print('Part 1:', validpass_part1, 'Part 2:', validpass_part2)
