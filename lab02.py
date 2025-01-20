import csv 
import pandas as pd

username = input("Enter your Username: ")
password = input("Enter your StudentNumber: ")

print("Choose an option:")
print("1. Read a file")
print("2. Write to a file")
choice = input("Enter 1 or 2: ")

def readfile():
    with open('inventory_data.csv', mode='r', newline='') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            print(",".join(row))  


def writefile():
    with open('inventory_data.csv', mode='w', newline='') as file:
        input = csv.writer(file)
    input.writerows(data)


data = pd.read_csv('inventory_data.csv')
data_dict = data.to_dict(orient='records')
print(readfile())
