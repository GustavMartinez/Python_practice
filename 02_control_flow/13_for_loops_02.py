#Average Height

#Input a Python list of student heights

student_heights = input().split()

#Conversion de cada uno de los elementos a integral. 
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#Suma:

Total_alturas = 0
Total_elementos = 0

for i in student_heights:
    Total_elementos += 1
    Total_alturas += i

average = round(Total_alturas/Total_elementos)

print(Total_alturas)
print(Total_elementos)
print(average)