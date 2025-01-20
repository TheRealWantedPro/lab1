import csv 
import pandas as pd



def readfile():
    with open('inventory_data.csv', mode ='r')as file:
        csvFile = csv.reader(file)
    for lines in csvFile:
            print(lines)


def writefile():
    with open('inventory_data', mode='w', newline='') as file:
        input = csv.writer(file)
    input.writerows(data)


data = pd.read_csv('inventory_data')
data_dict = data.to_dict(orient='records')
print(data_dict)
