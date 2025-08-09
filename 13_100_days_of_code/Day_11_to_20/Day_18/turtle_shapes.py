from turtle import Turtle, Screen
import random


ramon = Turtle()
ramon.shape("turtle")

colors = ["dark violet", "maroon", "aquamarine", "green", 'red']


vertices = 3

while vertices <= 10:

    ramon.color(random.choice(colors))
    for _ in range(vertices):
        ramon.fd(150)
        ramon.right(360/vertices)
    vertices += 1





mi_ventana = Screen()
mi_ventana.exitonclick()