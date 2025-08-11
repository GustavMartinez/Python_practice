# w = Forwards
# s = Backwards
# A = Counter-clockwise (left)
# D = Clockwise (right)
# c = Clear and center


import turtle as t

def move_forward():
    tom.fd(10)


def move_backward():
    tom.back(10)


def move_rigth():
    tom.right(10)


def move_left():
    tom.left(10)


def reset_ventana():
    ventana.resetscreen()


tom = t.Turtle()
ventana = t.Screen()


ventana.listen()
ventana.onkey(key='w', fun=move_forward)
ventana.onkey(key='s', fun=move_backward)
ventana.onkey(key='a', fun=move_left)
ventana.onkey(key='d', fun=move_rigth)
ventana.onkey(key='c', fun=reset_ventana)



ventana.exitonclick()



