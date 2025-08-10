from turtle import Turtle, Screen
import random

colors = ["dark violet", "maroon", "aquamarine", "green", 'red', "goldenrod"]



timmy = Turtle()
timmy.pensize(width=10)


for _ in range(100):
    timmy.color(random.choice(colors))
    timmy.fd(25)
    direction = random.randint(0,3)
    if direction == 0:
        timmy.rt(90)
    elif direction == 1:
        timmy.lt(90)
    elif direction == 2:
        timmy.back(25)




la_ventana = Screen()
la_ventana.exitonclick()