from tkinter import *

window = Tk()
window.title("GUI training")
window.minsize(500, 500)
window.config(padx=30, pady=100)

def change_text():
    user_text = input.get()
    my_label.config(text=user_text)

# Labels
my_label = Label(text='I am a Label', font=('Arial', 24))
my_label.grid(column=0, row=0)

# Buttons
my_button = Button(text='Click Me!', command=change_text)
my_button.grid(column=1, row=1)


new_button = Button(text="New Button").grid(column=2, row=0)

#Input
input = Entry(width=40)
input.grid(column=3, row=2)




window.mainloop()

