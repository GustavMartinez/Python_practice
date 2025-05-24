import turtle as t
from turtle import Screen
import random

t.colormode(255)



tim = t.Turtle()
tim.pensize(10)

for _ in range(200):

    x = random.randint(1,4)
    tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    if x == 1:
        tim.forward(30)
    elif x == 2:
        tim.right(90)
    elif x == 3:
        tim.left(90)
    else:
        tim.backward(30)



screen = Screen()
screen.title('Gusty')
screen.exitonclick()