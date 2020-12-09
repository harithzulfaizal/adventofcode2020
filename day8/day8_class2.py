import copy

class day8:
    def __init__(self, input_path):
        self.input = [i.split(' ') for i in open(input_path).read().splitlines()]

    def count_accumulator(self, instr, part=0):
        acc_count = 0
        j = 0  # start
        index_norpt = []
        nj = []

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
        elif part == 1:
            return acc_count
        else:
            return 0
        
    @property
    def part_one(self):
        instr = self.input

        count = self.count_accumulator(instr, 1)
        return count

    @property
    def part_two(self):
        const_instr = self.input
        nj = []
        for k, item in enumerate(const_instr):
            j = 0
            instr = copy.deepcopy(const_instr)

            if k not in nj:
                if instr[k][0] == 'jmp':
                    instr[k][0] = 'nop'
                    nj.append(k)
                elif instr[k][0] == 'nop':
                    instr[k][0] = 'jmp'
                    nj.append(k)

            count = self.count_accumulator(instr)
            if count != 0:
                break
        return count

if __name__ == "__main__":
    input_path = "day8_input.txt"
    input = day8(input_path)

    print('Task 1:', input.part_one)
    print('Task 2:', input.part_two)
