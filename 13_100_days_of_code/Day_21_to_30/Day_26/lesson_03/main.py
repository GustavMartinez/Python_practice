import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# dict comprehension
students_scores = {student:random.randint(1,100) for student in names}

print(students_scores)


# conditional dict comprehension
passed_students = {key:value for (key, value) in students_scores.items() if value > 60}

print(passed_students)