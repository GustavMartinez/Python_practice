from turtle import Turtle

STARTING_POSITION = (0, -280)
MISSIL_SPEED = 10  # Velocidad del misil


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('triangle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def fire(self):
        return Missil(self.xcor(), self.ycor() + 20)  # Devuelve el misil para control externo


class Missil(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.penup()
        self.goto(x, y)

    def move(self):
        new_y = self.ycor() + MISSIL_SPEED
        self.goto(self.xcor(), new_y)



