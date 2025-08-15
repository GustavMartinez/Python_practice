from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,coords):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(coords)


    def paddle_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)


    def paddle_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)