import turtle as t

tim = t.Turtle()
screen = t.Screen()


def  move_forwards():
    tim.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)



screen.exitonclick()