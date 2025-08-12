from turtle import Screen, Turtle
from snake_game_part_3_snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0) # turn of tracer


snake = Snake()


game_is_on = True


while game_is_on:
    screen.update() # Update screen
    time.sleep(0.1)

    snake.move()

screen.exitonclick()