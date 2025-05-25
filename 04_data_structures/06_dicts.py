# MINI PROJECT

"""

1. Check if "gpa" is in student. If it exists and is greater than 3.5, add "Advanced Python" to the courses.

2. Check if "graduated" is True. If so, print: "Congratulations on your graduation!".

3. Print the updated courses list.



"""


student = {
    "name": "Emma Johnson",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8,
    "graduated": False,
    "courses": ["Python", "Data Structures", "AI"],
    "contact": {
        "email": "emma.j@example.com",
        "phone": "555-1234"
    }
}

if "gpa" in student:
    if student["gpa"] > 3.5:
        student["courses"].append("Advanced Python")
    else:
        print("GPA lest than 3.5")

else:
    print("gpa is not available")

if student["graduated"] == True:
    print("Congratulations on your graduation!")
else:
    print("Keep going until you are graduated")

for course in student["courses"]:
    print(course)