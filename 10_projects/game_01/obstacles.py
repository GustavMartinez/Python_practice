from turtle import Turtle

STARTING_POSITION = [(100, 200), (50, 200), (0, 200), (-50, 200), (-100, 200)]


class Obstacle():
    def __init__(self):
        self.line_obstacles()

    def line_obstacles(self):
        for each in STARTING_POSITION:
            part = Turtle('square')
            part.color('white')
            part.penup()
            part.goto(each)
        
