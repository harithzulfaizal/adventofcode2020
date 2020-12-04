import pandas as pd
import re

with open("day4_input.txt") as f:
    input = f.read()

split_input = input.split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'] #cid is optional, else is required

i = 0
row_list = []
for data in split_input:
    data = data.replace("\n",  ' ').split(' ')
    dict_pp = dict(item.split(':') for item in data)
    row_list.append(dict_pp)

passport_data = pd.DataFrame(row_list)
passport_data = passport_data.where(passport_data.notnull(), None)

def part_one(df, fields):
    inv_count = 0
    for i in range(len(passport_data)):
        for field in fields:
            if passport_data.loc[i][field] == None:
                if field == 'cid':
                    continue
                else:
                    inv_count += 1
                    break

    valid_count = len(passport_data) - inv_count
    return valid_count

def valid_fields(name, val):
    if name == 'byr':
        return len(val) == 4 and val.isdigit() and 1920 <= int(val) <= 2002

    if name == 'iyr':
        return len(val) == 4 and val.isdigit() and 2010 <= int(val) <= 2020

    if name == 'eyr':
        return len(val) == 4 and val.isdigit() and 2020 <= int(val) <= 2030

    if name =='hgt':
        if 'cm' in val:
            cm = val.find('cm')
            yr = int(val[:cm])
            return 150 <= yr <= 193
        if 'in' in val:
            inch = val.find('in')
            yr = int(val[:inch])
            return 59 <= yr <= 76
        return False

    if name == 'hcl':
        pattern = re.compile("[a-f0-9]+")
        return len(val) == 7 and val[0] == '#' and bool(pattern.match(val[1:]))

    if name == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if name == 'pid':
        return len(val) == 9 and val.isdigit()

    if name == 'cid':
        pass

    return True

def part_two(df, fields):
    #rules = [byr, iyr, eyr, hgt, hcl, ecl, pid, cid]
    inv_count = 0
    for i in range(len(passport_data)):
        temp_data = [passport_data.loc[i][field] for field in fields]
        temp_data = ['0' if v is None else v for v in temp_data]
        temp_validity = [valid_fields(field, temp_data[i]) for i, field in enumerate(fields)]

        if False in temp_validity:
            inv_count += 1
        else:
            pass #check valids

    valid_count = len(passport_data) - inv_count
    return valid_count

def main():
    print('Part 1:', part_one(passport_data, fields))
    print('Part 2:', part_two(passport_data, fields))

if __name__ == "__main__":
    main()
