
# Dashed line and square

from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("green")


def linea():
    for _ in range(10):
        tommy.fd(10)
        tommy.penup()
        tommy.fd(10)
        tommy.pendown()

for _ in range(4):
    linea()
    tommy.right(90)


mi_ventana = Screen()
mi_ventana.exitonclick()