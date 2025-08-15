from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('circle')
        self.penup()
        self.home()
        self.down_up = 0



    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)



    def move_down(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)


    def bounce(self):

        if self.down_up == 0:
            self.move()
            print(self.ycor())
            if self.ycor() >= 300:
                self.down_up = 1
        else:
            self.move_down()
            print(self.ycor())
            if self.ycor() <= -300:
                self.down_up = 0
            