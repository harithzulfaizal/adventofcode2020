def read_file(filename):
    with open(filename) as f:
        return f.readlines()

input = 'day3_input.txt'
mapdata = read_file(input)
tree = '#'

print(mapdata)
width = len(mapdata[0])-1
tree_count = 0
i=0

for line in mapdata:
    if line[i] == tree:
        tree_count += 1

    i += 3
    i = i % width

print(tree_count)
slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]

tree2 = []
treeprod = 1
for slope in slopes:
    pos = [0, 0]
    tree_count2 = 0
    while pos[0] < len(mapdata):
        if mapdata[pos[0]][pos[1]] == tree:
            tree_count2 += 1

        pos[0] += slope[0]
        pos[1] += slope[1]

        pos[1] = pos[1] % width

    tree2.append(tree_count2)
    treeprod *= tree_count2

print(tree2)
print(treeprod)
