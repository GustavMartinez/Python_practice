# LIST OF DICTIONARIES

# Working with list of dictionaries:

students = [
    {"name":"Emma", "gpa": 3.8},
    {"name":"Liam", "gpa": 3.2},
    {"name": "Olivia", "gpa": 3.6}
]

# You can loop through the list and work with each dictionary:

for student in students:
    print(student["name"], student["gpa"])


new_students = [
    {"name": "Emma", "gpa": 3.8},
    {"name": "Liam", "gpa": 3.2},
    {"name": "Olivia", "gpa": 3.6},
    {"name": "Noah", "gpa": 2.9}
]

for new_student in new_students:
    print(new_student["name"], new_student["gpa"])

count = 0
for new_student in new_students:
    if new_student["gpa"] > 3.5:
        print("Top student:", new_student["name"], "with GPA:", new_student["gpa"])
        count += 1

print(f"There are a total of {count} top student/s")
