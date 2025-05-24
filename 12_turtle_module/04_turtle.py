from turtle import *


tortu = Turtle()

for _ in range(4):
    tortu.forward(200)
    tortu.right(90)

tor = Turtle()


for _ in range(10):
    tor.right(10)
    tor.forward(25)
    tor.up()
    tor.forward(25)
    tor.down()

screen = Screen()
screen.exitonclick()