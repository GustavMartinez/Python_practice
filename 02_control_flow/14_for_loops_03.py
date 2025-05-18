# Program that calculates the highest score from a list of scores.

#Input a list of student scores:

student_scores = input().split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

maximum_value = 0

for i in student_scores:
    if i > maximum_value:
        maximum_value = i

print(f"El maximo valor ingresado es:  {maximum_value}")