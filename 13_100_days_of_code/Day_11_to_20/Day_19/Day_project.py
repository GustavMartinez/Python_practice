import turtle as t
import random as r


is_race_on = False # inicio de la carrera

screen = t.Screen()

screen.setup(width=500, height=400) #screen size
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

initial_y = -150
initial_x = -230


for col in colors:
    turtle = t.Turtle(shape='turtle')
    turtle.color(col)
    turtle.penup()
    turtle.goto(x=initial_x, y=initial_y)
    initial_y += 50
    all_turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win")
            else:
                print(f"You lose. The {winning_color} turtle is the winner")

        random_distance = r.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()
