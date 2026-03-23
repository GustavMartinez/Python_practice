import tkinter as tk

window = tk.Tk()

# Title of the program
window.title("My program")

# sizes of the window
window.minsize(width=300, height=300)

# Specify the component and then packed
my_label = tk.Label(text="Bottom Label", font=("Arial", 24, "bold"), ) 
my_label.pack(side="bottom")


# Specify another component and then packed
second_label = tk.Label(text="Top label", font=("Arial", 15, "italic"))
second_label.pack(side="top")


# changing the value of the component, from top to left:
second_label.config(text="Left Label")
second_label.pack(side="left")


# Specify a button

def button_clicked():
    second_label.config(text="Right Label")
    second_label.pack(side="right")
    my_button.pack(side="top")
    user_input = input.get()
    my_label.config(text=user_input)

my_button = tk.Button(text="Click me", command=button_clicked)
my_button.pack(side="left")


# Entry text

input = tk.Entry(width=50)
input.pack()

# This need to be at the end
window.mainloop()
