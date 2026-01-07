import re
import random
import string
import json

# Load existing data
try:
    with open("students.json", "r") as f:
        student_list = json.load(f)
except FileNotFoundError:
    student_list = []

def save_data():
    with open("students.json", "w") as f:
        json.dump(student_list, f)

def add():
    print("Student MGMT System. To register, fill the following:")

    length = 6
    characters = string.ascii_letters + string.digits
    student_id = ''.join(random.choices(characters, k=length))

    Name = input("Enter your name: ")
    while Name == "" or re.search(r"\d", Name):
        ask = input("Name should not be empty or contain numbers. Retry? (Y/N): ").lower()
        if ask == "y":
            Name = input("Enter your name: ")
        else:
            print("Exiting registration.")
            return

    Age = input("Enter your age: ")
    while Age == "" or not Age.isdigit():
        ask = input("Age should not be empty and must be a number. Retry? (Y/N): ").lower()
        if ask == "y":
            Age = input("Enter your age: ")
        else:
            print("Exiting registration.")
            return

    Major = input("Enter your major: ")
    while Major == "" or re.search(r"\d", Major):
        ask = input("Major should not be empty or contain numbers. Retry? (Y/N): ").lower()
        if ask == "y":
            Major = input("Enter your major: ")
        else:
            print("Exiting registration.")
            return

    student = {
        "ID": student_id,
        "Name": Name,
        "Age": Age,
        "Major": Major
    }

    student_list.append(student)
    save_data()
    print("\nRegistration successful!")
    print(f"Student ID: {student_id}")
    print(f"Name: {Name}")
    print(f"Age: {Age}")
    print(f"Major: {Major}")

def display():
    if not student_list:
        print("No students registered yet.")
        return
    for student in student_list:
        print(f"ID: {student['ID']}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Major: {student['Major']}")
        print("-" * 20)

def edit():
    st_id = input("Enter the student ID that you want to edit: ")
    student_found = None
    for student in student_list:
        if student["ID"] == st_id:
            student_found = student
            break

    if not student_found:
        print("Student ID not found")
        return

    # Display current student info
    print("\nCurrent student details:")
    print(f"Name: {student_found['Name']}")
    print(f"Age: {student_found['Age']}")
    print(f"Major: {student_found['Major']}")
    
    field = input("\nWhat do you want to edit? (Name/Age/Major): ").strip().lower()
    
    if field == "name":
        new_name = input("Enter the new name: ")
        while new_name == "" or re.search(r"\d", new_name):
            ask = input("Name should not be empty or contain numbers. Retry? (Y/N): ").lower()
            if ask == "y":
                new_name = input("Enter the new name: ")
            else:
                print("Edit cancelled.")
                return
        student_found["Name"] = new_name
        
    elif field == "age":
        new_age = input("Enter the new age: ")
        while new_age == "" or not new_age.isdigit():
            ask = input("Age should not be empty and must be a number. Retry? (Y/N): ").lower()
            if ask == "y":
                new_age = input("Enter the new age: ")
            else:
                print("Edit cancelled.")
                return
        student_found["Age"] = new_age
        
    elif field == "major":
        new_major = input("Enter the new major: ")
        while new_major == "" or re.search(r"\d", new_major):
            ask = input("Major should not be empty or contain numbers. Retry? (Y/N): ").lower()
            if ask == "y":
                new_major = input("Enter the new major: ")
            else:
                print("Edit cancelled.")
                return
        student_found["Major"] = new_major
        
    else:
        print("Invalid field selected. Edit cancelled.")
        return
    
    save_data()
    print("\nStudent details updated successfully!")

def remove():
    st_id = input("Enter the student ID you want to remove: ")
    student_found = None
    for student in student_list:
        if student["ID"] == st_id:
            student_found = student
            break

    if student_found:
        student_list.remove(student_found)
        save_data()
        print(f"Student with ID {st_id} has been removed.")
    else:
        print("Student ID not found.")

# Main menu loop
while True:
    print("\nStudent MGMT System")
    print("1. Enter")
    print("2. Display")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")

    Number = input("Enter one of the options: ")
    if Number == "1":
        add()
    elif Number == "2":
        display()
    elif Number == "3":
        edit()
    elif Number == "4":
        remove()
    elif Number == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid option. Try again.")
