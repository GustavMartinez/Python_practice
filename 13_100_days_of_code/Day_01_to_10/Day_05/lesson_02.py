student_scores = [180, 124, 165, 173, 325, 189, 25, 169, 60, 146, 250]



# Calcular el máximo valor

score = 0

for student in student_scores:
    if student > score:
        score = student

print(score)



# Calcular el menor valor

new_score = 0

for student_b in student_scores:
    if new_score <= 0:
        new_score = student_b
    else:
        if new_score > student_b:
            new_score = student_b

print(new_score)
