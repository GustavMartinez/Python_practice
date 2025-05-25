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


##########################################

# checking key existence and using .get()

# check if a key exists:
if 'gpa' in student:
    print("GPA is available")
if 'parents' in student:
    print("parents is available")
else:
    print("parents is not available")

# use .get() to access a key safely:
print(student.get("nickname", "Not found"))


if 'email' in student["contact"]:
    print("email is available")
else:
    print("email is not available")

print(student["contact"].get("phone", "not provided"))
print(student.get("linkedin", "Not provided"))

#########################################

# Working with nested structures:

# Access nested data:
print(student["contact"]["email"])

# Access items in a list inside a dictionary:
for course in student["courses"]:
    print(course)

# Add or remove items from the list:
student["courses"].append("Math")
# student["courses"].remove("AI")

for course in student["courses"]:
    print(course)


print(student["contact"]["email"])

for course in student["courses"]:
    print(course)

student["courses"].append("Databases")
student["courses"].remove("AI")
print(student["courses"])