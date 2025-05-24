# Importar todas las clases del modulo "turtle"

from turtle import *

# Se pueden importar clases específicas asi:
# from turtle import Turtle
# from turtle import Screen

# object timy created with the class turtle
# object my_screen created with the class screen
timy = Turtle()

timy.shape("turtle")

timy.width(3)
timy.color("chocolate")
timy.forward(100)
timy.right(90)
timy.forward(100)
timy.right(90)
timy.forward(100)
timy.right(90)
timy.width(5)
timy.color("red")
timy.forward(200)
timy.left(90)
timy.width(3)
timy.color("chocolate")
timy.forward(100)
timy.left(90)
timy.forward(100)
timy.left(90)
timy.forward(100)





my_screen = Screen()



print(my_screen.canvheight)
my_screen.exitonclick()