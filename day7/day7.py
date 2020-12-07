def part_one(bags_rules):
    validbags = ['shiny gold']

    j = 0
    while j < len(validbags):
         for bag in bag_bags:
             if bag[1].find(validbags[j]) != -1 and bag[0] not in validbags:
                 validbags.append(bag[0])
         j += 1

    return (len(validbags)-1)

def part_two(bags_rules):
    for bag in bag_bags:
        temp_bag = []
        x = bag[1].split(', ')
        num = [int(item[0:2]) for item in x if 'no other' not in item]
        typebag = [item[2:] for item in x if 'no other' not in item]

        for k, n in enumerate(num):
            temp_bag.append((typebag[k], n))

        bags[bag[0]] = temp_bag
    return bag_count('shiny gold')

def bag_count(mainbag):
    if mainbag in valid_bags:
        return valid_bags[mainbag]

    counter = 0
    for inner in bags[mainbag]:
        counter += inner[1] + inner[1] * bag_count(inner[0])

    valid_bags[mainbag] = counter
    return counter

if __name__ == "__main__":
    input = "day7_input.txt"
    bags_rules = [i.replace(' bags', '').replace(' bag', '').replace('.', '') for i in open(input).read().splitlines()]
    bag_bags = [x.split(' contain ') for x in bags_rules]

    bags = {}
    valid_bags = {}
    print('Part One:', part_one(bag_bags))
    print('Part Two:', part_two(bag_bags))
