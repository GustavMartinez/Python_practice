# w = Forwards
# s = Backwards
# A = Counter-clockwise (left)
# D = Clockwise (right)
# c = Clear and center

import turtle as t

tom = t.Turtle()
ventana = t.Screen()



def move_forward():
    tom.fd(10)

def move_back():
    tom.back(10)

def move_right():
    tom.right(10)

def move_left():
    tom.left(10)


def reset():
    ventana.resetscreen()



ventana.listen()
ventana.onkey(key='w', fun=move_forward)
ventana.onkey(key='s', fun=move_back)
ventana.onkey(key='a', fun=move_left)
ventana.onkey(key='d', fun=move_right)
ventana.onkey(key='c', fun=reset)






ventana.exitonclick()
