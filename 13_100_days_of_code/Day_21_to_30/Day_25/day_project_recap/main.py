import turtle
import pandas as pd

# path to image
PATH_IMG = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project_recap/blank_states_img.gif'

# path to csv file
PATH_CSV = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project_recap/50_states.csv'

# path to save file with missing guesses:
PATH_TO_SAVE = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project_recap/'


# Creating the image background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = PATH_IMG
screen.addshape(image)
turtle.shape(image)


# Get csv file in pandas
data = pd.read_csv(PATH_CSV)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    # get answer from user:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="what's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(f"{PATH_TO_SAVE}states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


