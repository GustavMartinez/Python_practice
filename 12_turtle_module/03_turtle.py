from turtle import *

tor = Turtle()


for _ in range(10):
    tor.forward(25)
    tor.up()
    tor.forward(25)
    tor.down()


screen = Screen()
screen.exitonclick()