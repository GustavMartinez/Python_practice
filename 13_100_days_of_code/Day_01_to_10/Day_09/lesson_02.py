
"""

Write a program that converts their scores to grades.

This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 

- Scores 81 - 90: Grade = "Exceeds Expectations" 

- Scores 71 - 80: Grade = "Acceptable" 

- Scores 70 or lower: Grade = "Fail" 

"""


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,
    'Gadarel': 99
}

student_grades = {}


for k,v in student_scores.items():
    if v <= 70:
        student_grades[k] = "Fail"
    elif v > 70 and v < 80:
        student_grades[k] = "Acceptable"
    elif v > 80 and v < 90:
        student_grades[k] = "Exceeds Expectations"
    elif v > 90 and v < 100:
        student_grades[k] = "Outstanding"


print(student_grades)