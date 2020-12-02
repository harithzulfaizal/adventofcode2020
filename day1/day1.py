import pandas as pd

listyr = pd.read_csv("list_adventday1.csv", header=None)

years = list(listyr.iloc[:,0])
product1 = []
product2 = []

for i, yr in enumerate(years):
    for j, yr2 in enumerate(years[i:]):
            if yr+yr2 == 2020:
                product1.append(yr*yr2)
        for k, yr3 in enumerate(years[j:]):
            if yr+yr2+yr3 == 2020:
                product2.append(yr*yr2*yr3)

print("Task 1:", product1, "Task 2:", product2)
