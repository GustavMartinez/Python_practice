# Creating a square

from turtle import Turtle, Screen



timmy = Turtle()
timmy.shape("turtle")

for _ in range(4):
    timmy.fd(100)
    timmy.rt(90)


screen = Screen()
screen.exitonclick()