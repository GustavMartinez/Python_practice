import tkinter as tk

window = tk.Tk()
window.title("Mile to Km converter")
window.minsize(width=500, height=300)



# Label 1
equality_label = tk.Label(text="is equal to:", font=('Arial', 15, 'bold'))
equality_label.grid(column=0, row=1)


# Label 2
miles_label = tk.Label(text='Miles', font=("Arial", 15, 'bold'))
miles_label.grid(column=2, row=0)


# Label 3
km_label = tk.Label(text='Km', font=('Arial', 15, 'bold'))
km_label.grid(column=2, row=1)


# Label 4 - number to calculate
number_in_km = tk.Label(text=0, font=('Arial', 15, 'bold'))
number_in_km.grid(column=1, row=1)


# Button - calculate
button = tk.Button(text='Calculate')
button.grid(column=1, row=2)







window.mainloop()