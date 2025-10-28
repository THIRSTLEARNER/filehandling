# from csv import DictWriter, reader
# import os

# file = "record.csv"

# file_exists = os.path.exists(file)
# is_empty = os.path.getsize(file) == 0 if file_exists else True

# try:
#     with open(file, 'a',newline='') as files:
#         header = ["NAME","GRADE"]
#         write = DictWriter(files, fieldnames=header)
#         if is_empty:
#             write.writeheader()
#         name = input("Enter Your name: ")
#         grade = input("Enter Your Grade: ")  

#         write.writerow({"NAME": name,
#                         "GRADE": grade}) 
#     with open(file, 'r') as files:
#         read = reader(files)
#         print("All Records:")
#         for row in read:
#             print(row)

# except FileNotFoundError: 
#     print("file not found please enter file")

# except PermissionError:
#     print("Error: The file 'records.csv' is locked or cannot be accessed.")

# except Exception as e:
#     print(f"An unexpected error occurred: {e}")



import csv

try:
    # Expectation: The program will try to read the file first
    # If it exists, it will show the existing records
    with open("records.csv", "r") as file:
        print("Existing Records:")
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Expectation: If the file does not exist, the program should handle the error nicely
# It will create a new 'records.csv' file and add a header
except FileNotFoundError:
    print("File not found. Creating a new 'records.csv' file...")
    with open("records.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Grade"])
        print("New file created successfully!\n")

try:
    # Expectation: After making sure the file exists, the program will now ask for input
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    # Expectation: The program will add the new record to the CSV file
    with open("records.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])
        print("\nRecord saved successfully!\n")

    # Expectation: The program will display all records after saving
    with open("records.csv", "r") as file:
        print("All Records:")
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Expectation: If the file is open or locked, the program should not crash
# It will show a message instead
except PermissionError:
    print("Error: The file is locked or open in another program. Please close it first.")

# Expectation: If there’s any other error, it should also be caught and displayed nicely
except Exception as e:
    print(f"Something went wrong: {e}")
