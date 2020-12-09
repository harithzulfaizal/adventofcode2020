class day9:
    def __init__(self, input_path):
        self.data = list(map(int, open(input_path).read().splitlines()))

    def show(self):
        return self.data

    def sum_in_a_list(self, val, lst):
        tf = []
        for i in range(0, len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] != lst[j]:
                    if val-lst[i]-lst[j] == 0:
                        tf.append(True)
                    else:
                        tf.append(False)
        if True not in tf:
            return val, False

    def part_one(self, rnge):
        data = self.data

        k = 0
        for x in range(rnge, len(data)):
            rnge_lst = data[k:k+rnge]
            k += 1

            check = self.sum_in_a_list(data[x], rnge_lst)
            if type(check) == tuple:
                numb4 = data[x-1]
                self.invalid_val = check
                break

        return self.invalid_val[0]

    def part_two(self):
        invalid= self.invalid_val[0]
        data = self.data

        for i in range(len(data)):
            summ = data[i]
            contiguous_lst = []
            contiguous_lst.append(data[i])
            for j in range(i+1, len(data)):
                contiguous_lst.append(data[j])
                summ += data[j]
                if summ == invalid and len(contiguous_lst)>=2:
                    #print(summ, invalid, contiguous_lst)
                    return (max(contiguous_lst)+min(contiguous_lst))

        print('out')


if __name__ == "__main__":
    input_path = "day9_input.txt"
    data = day9(input_path)

    print('Task One:', data.part_one(25))
    print('Task Two:', data.part_two())


