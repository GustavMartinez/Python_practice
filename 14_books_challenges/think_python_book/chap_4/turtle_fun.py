import turtle


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.right(360/n)



sides = int(input('number of sides: '))
leng = int(input('Length of the segment: '))

screen = turtle.Screen()
bob = turtle.Turtle()

polygon(bob, leng, sides)


screen.exitonclick()