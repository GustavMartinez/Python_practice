from turtle import *
import random

colores = ['red', 'blue', 'yellow', 'green']


tim = Turtle()



def shapes(n):
    for _ in range(n):
        tim.forward(100)
        tim.right(360/n)

x = 3
while x >= 0 and x < 11:
    tim.color(random.choice(colores))
    shapes(x)
    x += 1




screen = Screen()
screen.exitonclick()