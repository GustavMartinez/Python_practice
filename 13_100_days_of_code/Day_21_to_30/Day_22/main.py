from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

game_is_on = True


screen.listen()
screen.onkey(r_paddle.paddle_up, key="Up")
screen.onkey(r_paddle.paddle_down, key="Down")

screen.onkey(l_paddle.paddle_up, key="w")
screen.onkey(l_paddle.paddle_down, key="s")

while game_is_on:
    screen.update()


screen.exitonclick()