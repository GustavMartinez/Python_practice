import turtle
import pandas as pd

PATH_IMAGE = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project/blank_states_img.gif'
PATH_DATA = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project/50_states.csv'
PATH_STATES_TO_LEARN = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project/'

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=500)

screen.addshape(PATH_IMAGE)
turtle.shape(PATH_IMAGE)

data = pd.read_csv(PATH_DATA)
all_states = data['state'].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(f"{PATH_STATES_TO_LEARN}states to learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]

        t.goto(state_data['x'].item(), state_data['y'].item())
        t.write(answer_state)




screen.exitonclick()