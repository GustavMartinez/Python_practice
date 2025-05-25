# FREQUENCY COUNTER

# Count how many times each course appears in a list using a dictionary.

course_list = [
    "Python", "AI", "Python", "Math",
    "AI", "Python", "Databases", "AI"
]

dictionary = {}

for course in course_list:
    if course not in dictionary:
        dictionary[course] = 1
    else:
        dictionary[course] = dictionary[course] + 1

print(dictionary)