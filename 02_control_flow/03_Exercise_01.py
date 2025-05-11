# BMI = weight (kg)/height**2 (m**2)

height = float(input("Ingrese la altura: "))
weight = float(input("Ingrese su peso: "))

BMI = weight/height**2

if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal weight")
elif BMI < 30:
    print("slightly overweight")
elif BMI < 35:
    print("Obese")
else:
    print("clinically obese")


print(round(BMI, 3))