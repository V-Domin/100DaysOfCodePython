from tkinter import *

window = Tk()
window.title("Miles to Km Project")
window.config(padx=150, pady=60)


def converter():
    number = number_input.get()
    result = int(number) * 1.6
    result_text.config(text=int(result))


number_input = Entry()
number_input.grid(column=1, row=0, padx=10, pady=10)
number_input.focus()


miles_label = Label(text="Miles", font=('Arial', 12))
miles_label.grid(column=2, row=0, padx=10, pady=10)

is_equal_text = Label(text="is equal to", font=('Arial', 12))
is_equal_text.grid(column=0, row=1, padx=10, pady=10)

result_text = Label(text='0', font=('Arial', 12))
result_text.grid(column=1, row=1, padx=10, pady=10)

km_label = Label(text="Km", font=('Arial', 12))
km_label.grid(column=2, row=1, padx=10, pady=10)

calculate_button = Button(text='Calculate', command=converter)
calculate_button.grid(row=2, column=1, padx=10, pady=10)






window.mainloop()