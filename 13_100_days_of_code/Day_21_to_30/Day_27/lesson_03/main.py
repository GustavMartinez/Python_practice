import tkinter as tk

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


# Label
my_label = tk.Label(text="I am a Label", font=('Arial', 24, 'bold'))
# my_label.pack()
my_label.place(x=0, y=0)



# Button
button = tk.Button(text="Click me", command=button_clicked)
# button.pack()
button.place(x=300, y=0)


# Entry
input = tk.Entry(width=10)
print(input.get())
input.pack()



window.mainloop()