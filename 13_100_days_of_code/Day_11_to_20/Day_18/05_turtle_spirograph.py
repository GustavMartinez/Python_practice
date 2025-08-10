import turtle as t
import random as r
t.colormode(255)

def colors():
    red = r.randint(0,255)
    blue = r.randint(0,255)
    green = r.randint(0,255)

    return (red, blue, green)

tom = t.Turtle()


while True:
    tom.circle(100)
    tom.right(360/3)
    tom.color(colors())
    print(tom.heading())
    if tom.heading() == 0.0:
        break
   






ventana = t.Screen()
ventana.exitonclick()

