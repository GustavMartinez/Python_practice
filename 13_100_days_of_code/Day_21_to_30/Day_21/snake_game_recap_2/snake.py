from turtle import Turtle


STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITION:
                segment = Turtle("square")
                segment.color("white")
                segment.penup()
                segment.goto(position)
                self.segments.append(segment)


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1): # range(start, stop, step)
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
         if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
         if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
         if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
    
    def right(self):
         if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)