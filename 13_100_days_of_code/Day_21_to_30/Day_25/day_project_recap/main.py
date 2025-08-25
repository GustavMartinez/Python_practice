import turtle

# path to image
PATH_IMG = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/day_project_recap/blank_states_img.gif'


# Creating the image background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = PATH_IMG
screen.addshape(image)
turtle.shape(image)






screen.exitonclick()
