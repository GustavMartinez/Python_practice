import tkinter as tk

window = tk.Tk()
window.title("My second GUI pro")
window.minsize(width=500, height=300)

#My label
my_label = tk.Label(text="A label", font=("Arial", 24, 'bold'))
my_label.pack(side='left')


# change the text of the label

my_label['text'] = 'new text' # ... or
my_label.config(text='new new text')



def button_clicked():
    print("I got clicked")
    #my_label.config(text='I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)
    my_label.pack(side='right')



button = tk.Button(text="click me", command=button_clicked)
button.pack()


# Entry component

input = tk.Entry(width=10)
input.pack()



window.mainloop()