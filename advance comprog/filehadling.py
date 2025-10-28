import os
import csv

filename = "data1.csv"
header = ["name", "age", "grade"]


file_exists = os.path.exists(filename)
is_empty = os.path.getsize(filename) == 0 if file_exists else True
while True:
        
        with open(filename, "r") as file1:
                reader = csv.DictReader(file1)
                print("\nFAILED STUDENTS:")
                for row in reader:
                    if int(row["grade"]) < 75:
                        print(row["name"], "-", row["grade"])

        with open(filename, "r") as file2:
                reader = csv.DictReader(file2)
                print("\nPASSED STUDENTS:")
                for row in reader:
                    if int(row["grade"]) >= 75:
                        print(row["name"], "-", row["grade"])
        
        enter = input("do you want to enter data?(type1) ")
        if enter == '1':
            
            with open(filename, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header)

                # Only write header if file is new or empty
                if is_empty:
                    writer.writeheader()

                name = input("Enter your name: ")
                age = input("Enter your age: ")
                grade = input("Enter your grade: ")

                writer.writerow({
                    "name": name,
                    "age": age,
                    "grade": grade
                })
   
        else:
            raise TypeError("PLEASE TYPE 1") 
                #kelly

                
            
