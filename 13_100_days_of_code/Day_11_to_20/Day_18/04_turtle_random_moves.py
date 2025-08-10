import turtle as t
import random

t.colormode(255)

# colors = ["dark violet", "maroon", "aquamarine", "green", 'red', "goldenrod"]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

timmy = t.Turtle()
timmy.pensize(width=10)


for _ in range(100):
    timmy.color(random_color())
    timmy.fd(25)
    direction = random.randint(0,3)
    if direction == 0:
        timmy.rt(90)
    elif direction == 1:
        timmy.lt(90)
    elif direction == 2:
        timmy.back(25)




la_ventana = t.Screen()
la_ventana.exitonclick()