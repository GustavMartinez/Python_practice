from turtle import Turtle, Screen
import random

colors = ["dark violet", "maroon", "aquamarine", "green", 'red', "goldenrod"]


timmy = Turtle()
timmy.pensize(width=10)


for _ in range(5):
    timmy.color(random.choice(colors))
    timmy.fd(50)
    timmy.right(90)



la_ventana = Screen()
la_ventana.exitonclick()