import csv 
import pandas as pd

username = input("Enter your Username: ")
password = input("Enter your StudentNumber: ")
with open('user_data.csv', 'w') as file:
        file.write(username)
        file.write(password)

print("Choose an option:")
print("1. Display Product Inventory")
print("2. Add to Product Inventory")
choice = input("Enter 1 or 2: ")

if choice == "1":
    try:
        with open('inventory_data.csv', mode='r', newline='') as file:
            csvFile = csv.reader(file)
            for row in csvFile:
                print(",".join(row))
    except FileNotFoundError:
        print("Error: File not found.")
elif choice == "2":
    content = input("Enter Product: ")
    with open('inventory_data.csv', 'w') as file:
        file.write(content)
    print("Product Added  to file successfully.")
else:
    print("Invalid choice. Please enter 1 or 2.")


data = pd.read_csv('inventory_data.csv')
data_dict = data.to_dict(orient='records')

