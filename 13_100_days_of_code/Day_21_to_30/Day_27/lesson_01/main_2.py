import tkinter

window = tkinter.Tk()



my_label = tkinter.Label(text="I am a label", font=("Arial", 50, "bold"))
my_label.pack()

second_label = tkinter.Label(text="I am another label", font=("Arial", 25, 'italic'))
second_label.pack(side='bottom')

other_label = tkinter.Label(text="This is one more label", font=("Arial", 15, 'italic'))
other_label.pack(side='left')


window.title("Second GUI program")
window.minsize(width=500, height=300) # size of the window
window.mainloop() # this keep the window on screen