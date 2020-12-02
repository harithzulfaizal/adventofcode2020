import pandas as pd

test_input = pd.read_csv("day2_input.csv", delim_whitespace=True, header=None)
#col 0 is min-max, col 1 is the letter, col 2 is the password
print(test_input.iloc[0,2])

total = len(test_input)
print(total)
#part1
'''
numlegit_password = 0
for i in range(total):
    password = test_input.iloc[i,2]
    limit = test_input.iloc[i,0].split('-')
    limit = [int(x) for x in limit] #0 min 1 max

    letter = test_input.iloc[i,1].replace(':','')

    counter = password.count(letter) #min<counter<max

    if counter>= limit[0] and counter<=limit[1]:
        numlegit_password+=1

print(numlegit_password)
'''

#part2
numlegit_password = 0
for i in range(total):
    #no index zero, so the index of the password should be +1 or position -1
    password = test_input.iloc[i,2]
    position = test_input.iloc[i,0].split('-')
    position = [int(x) for x in position] #0 min 1 max

    letter = test_input.iloc[i,1].replace(':','')

    #ONLY one of the letter, two -invalid
    if letter == password[position[0]-1] or letter == password[position[1]-1]:
        if password[position[0]-1] != password[position[1]-1]:
            print(letter, password[position[0]-1], password[position[1]-1])
            numlegit_password+=1

print(numlegit_password)



