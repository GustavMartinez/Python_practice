from turtle import Turtle

FONT = ('Arial', 15, 'normal')
ALIGN = 'center'



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.snake_score}", align=ALIGN, font=FONT)
        
    def score(self):
        self.snake_score += 1
        self.write(f"Score: {self.snake_score}", align=ALIGN, font=FONT)