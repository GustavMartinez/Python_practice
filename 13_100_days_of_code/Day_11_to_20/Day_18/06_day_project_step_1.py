# Extract the colors with colorgram

import colorgram

rgb_colors = []

colors = colorgram.extract('/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_11_to_20/Day_18/image.jpg', 40)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


print(rgb_colors)