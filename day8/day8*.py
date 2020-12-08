def read_file(input_path):
    return [i.split(' ') for i in open(input_path).read().splitlines()]


def part_one(instr):
    acc_count = 0
    j = 0 #start
    global index_norpt
    index_norpt = []

    while j not in index_norpt:
        index_norpt.append(j)
        name, amt = instr[j][0], instr[j][1]
        if name == 'acc':
            acc_count += int(amt)
            j += 1
            name, amt = instr[j][0], instr[j][1]
        if name == 'nop':
            j += 1
            name, amt = instr[j][0], instr[j][1]
        if name == 'jmp':
            j += int(amt)
            name, amt = instr[j][0], instr[j][1]

    return acc_count, instr

def count_two(instr):
    acc_count = 0
    j = 0
    local_visited = []
    while j not in local_visited and j < len(instr):
        local_visited.append(j)
        name = instr[j][0]
        amt = int(instr[j][1])
        if name == 'acc':
            acc_count += amt
            j += 1
        elif name == 'jmp':
            j += amt
        else:
            j += 1
    if j not in local_visited:
        print(acc_count)

def part_two(instr):
    for v in index_norpt[::-1]:
        changednj = instr
        if changednj[v][0] == 'jmp':
            changednj[v][0] = 'nop'
            count_two(changednj)
        elif changednj[v][0] == 'nop':
            changednj[v][0] = 'jmp'
            count_two(changednj)


if __name__ == "__main__":
    input_path = "day8_input.txt"
    input = read_file(input_path)

    print(part_one(input)[0])
    part_two(input)

