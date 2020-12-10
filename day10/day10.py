from collections import Counter

class Day10:
    def __init__(self, input_path):
        self.jolts = list(set(map(int, open(input_path).read().splitlines())))
        self.max_adpt = max(self.jolts) + 3
        self.jolts.append(self.max_adpt)

    def show(self):
        return self.jolts, self.max_adpt

    def part_one(self):
        chargoutlet = 0
        dif1 = []
        dif3 =[]

        numb4 = chargoutlet
        for num in self.jolts:
            if num - numb4 == 1:
                dif1.append(num)
            elif num - numb4 == 3:
                dif3.append(num)

            numb4 = num

        return len(dif1), len(dif3), len(dif1)*len(dif3)

    def part_two(self):
        distinct_arrgmt = Counter()
        distinct_arrgmt[0] = 1

        for j in self.jolts:
            distinct_arrgmt[j] = distinct_arrgmt[j-1] + distinct_arrgmt[j-2] + distinct_arrgmt[j-3]

        return distinct_arrgmt[self.jolts[-1]]



if __name__ == "__main__":
    input_path = "day10_input.txt"
    input = Day10(input_path)
    #print(input.show()[1])

    print("Task One:", input.part_one()[2])
    print("Task Two:", input.part_two())
