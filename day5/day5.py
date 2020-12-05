import pandas as pd

with open("day5_input.txt") as f:
    boarding_passes = f.read().split('\n')

boarding_df = pd.DataFrame()
boarding_df['Full ID'] = boarding_passes
boarding_df['Row ID'] = [x[0:7] for x in boarding_passes]
boarding_df['Col ID'] = [x[7:] for x in boarding_passes]

print(boarding_df.head())

def element_inlst(x):
    return int(len(x)/2) if len(x)%2 == 0 else int((len(x)+1)/2)

split_id = lambda lst: [lst[i:i+element_inlst(lst)] for i in range(0, len(lst), element_inlst(lst))]

def check_rowcol(string, end):
    rowcol = split_id(list(range(end)))
    for val in string:
        if val == 'F' or val == 'L':
            rowcol = split_id(rowcol[0])
        else:
            rowcol = split_id(rowcol[1])
    return rowcol[0][0]

row, col = [], []
seat_id = []
for j in range(len(boarding_df)):
    temp_col = check_rowcol(boarding_df.iloc[j]['Col ID'], 8)
    temp_row = check_rowcol(boarding_df.iloc[j]['Row ID'], 128)
    seat = temp_row*8 + temp_col

    row.append(temp_row)
    col.append(temp_col)
    seat_id.append(seat)

boarding_df['Row'] = row
boarding_df['Col'] = col
boarding_df['Seat ID'] = seat_id

print('Part One:', boarding_df['Seat ID'].max())

seat_sorted = list(set(boarding_df['Seat ID']))

def missing_seat(lst):
    start , end = lst[0], lst[-1]
    return sorted(set(range(start, end + 1)).difference(lst))

print('Part Two:', missing_seat(seat_sorted)[0])
