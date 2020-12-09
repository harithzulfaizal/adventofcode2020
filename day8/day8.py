import copy

class day8:
    def __init__(self, input_path):
        self.input = [i.split(' ') for i in open(input_path).read().splitlines()]

    @property
    def part_one(self):
        acc_count = 0
        instr = self.input
        j = 0 #start
        index_norpt = []
        nj = []

        while j not in index_norpt:
            index_norpt.append(j)
            name, amt = instr[j][0], instr[j][1]
            if name == 'acc':
                acc_count += int(amt)
                j += 1
            if name == 'nop':
                j += 1
            if name == 'jmp':
                j += int(amt)

        return acc_count, instr

    @property
    def part_two(self):
        const_instr = self.input
        nj = []
        for k, item in enumerate(const_instr):
            j = 0
            acc_count = 0
            index_norpt = []
            instr = copy.deepcopy(const_instr)

            if k not in nj:
                if instr[k][0] == 'jmp':
                    instr[k][0] = 'nop'
                    nj.append(k)
                elif instr[k][0] == 'nop':
                    instr[k][0] = 'jmp'
                    nj.append(k)

            try:
                while j not in index_norpt and j < len(instr):
                    index_norpt.append(j)
                    name, amt = instr[j][0], instr[j][1]
                    if name == 'acc':
                        acc_count += int(amt)
                        j += 1
                    if name == 'nop':
                        j += 1
                    if name == 'jmp':
                        j += int(amt)
                if j not in index_norpt:
                    return acc_count
            except IndexError:
                #print('here')
                return (acc_count)

if __name__ == "__main__":
    input_path = "day8_input.txt"
    input = day8(input_path)

    print('Task 1:', input.part_one[0])
    print('Task 2:', input.part_two)
