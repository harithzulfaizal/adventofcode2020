def split_groups(path_input):
    with open(path_input) as f:
        return f.read().split('\n\n')

def count_yes(neslst):
    biglst = []
    for lst in neslst:
        for l in lst:
            biglst.append(l)

    count = len(set(biglst))
    return count

def part_one(groups):
    big_yes = []
    for gp in groups:
        yesses = []
        for person in gp:
            yesses.append(list(person))

        count = count_yes(yesses)
        big_yes.append(count)
    return big_yes

def part_two(groups): #only count questions which everyone answered yes to
    count = 0

    for gp in groups:
        repeatedletter = {}
        for person in gp:
            for let in person:
                if let in repeatedletter:
                    repeatedletter[let] += 1
                else:
                    repeatedletter[let] = 1

        for key in repeatedletter:
            if repeatedletter[key] == len(gp):
                count += 1

    return count

if __name__ == '__main__':
    path_input = "day6_input.txt"
    groups = split_groups(path_input)
    groups = [x.split('\n') for x in groups] #list of people in group list

    print('Part One:', sum(part_one(groups)))
    print('Part Two:', part_two(groups))
