import pandas as pd

listyr = pd.read_csv("list_adventday1.csv", header=None)

years = list(listyr.iloc[:,0])
product = []

for i, yr in enumerate(years):
    for j, yr2 in enumerate(years[i:]):
        for k, yr3 in enumerate(years[j:]):
            if yr+yr2+yr3 == 2020:
                product.append(yr*yr2*yr3)

print(product)