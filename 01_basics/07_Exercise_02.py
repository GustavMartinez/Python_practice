import math

# CALCULATE THE CIRCUNFERENCE OF A CIRCLE

radius = float(input("Enter the radius of a circle: "))

circunference = 2 * math.pi * radius

print(f"The circunference is: {round(circunference, 2)}")


# CALCULATE THE AREA OF A CIRCLE

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area is {round(area, 3)}")


# CALCULATE THE HIPPOTENUSA

a = float(input('a'))
b = float(input('b'))

c = math.sqrt(pow(a,2)+pow(b,2))

print(c)