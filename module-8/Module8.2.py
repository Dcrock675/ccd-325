import json

# Function to print all students
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print()  # for spacing

# Load the JSON file
with open("student.json", "r") as file:
    students = json.load(file)

# Print original list notification
print("Original Student List\n")
print_students(students)

# Append new student (use SAME key names as the JSON file)
new_student = {
    "F_Name": "Drew",
    "L_Name": "Morrow",
    "Student_ID": 99999,
    "Email": "drew.morrow@gmail.com"
}
students.append(new_student)

# Print updated list notification
print("Updated Student List\n")
print_students(students)

# Write updated list back to JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("student.json file has been updated.")
