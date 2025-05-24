# Spirograph

import turtle as t
from turtle import Screen


tim = t.Turtle()

#tim.circle(50)

#while tim.xcor != 0:
#    tim.left(10)
#    tim.circle(50)
#    print(tim.xcor())
    

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(50)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


spirograph(50)


screen = Screen()
screen.exitonclick()