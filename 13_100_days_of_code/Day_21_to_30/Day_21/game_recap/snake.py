from turtle import Turtle

STARTING_POSITION = [(0,0), (-20, 0), (-40,0)]



class Snake:
    
    def __init__(self):
        self.segments = []

        for position in STARTING_POSITION:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) -1 , 0 , -1): # range va de 2 a 0, con -1 a la vez.
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)