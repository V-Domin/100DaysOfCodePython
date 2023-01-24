from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for letter in range(nr_letters)]
    password_symbol = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_number = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = password_number + password_letter + password_symbol
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    name_website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        name_website: {
            "email":email,
            "password":password
        }
    }

    if len(name_website) == 0 or len(password) == 0:
        messagebox.showwarning("Oops", "Please, don't leave any fields empty!")
    else:
        try:
            with open("data.json", 'r') as file:
                # 1) Read old data
                data = json.load(file)
                # 2) Update old data with the new one
                data.update(new_data)
                # 3) Save updated data
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    name_website = website_input.get()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            if name_website in data:
                email = data[name_website]['email']
                password = data[name_website]['password']
                messagebox.showinfo(f"{name_website}", f"Your email{email}\nYour password:{password}")
            else:
                messagebox.showwarning("Opps", "No details for the website exists")
    except FileNotFoundError:
        messagebox.showwarning("Error", "No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

website_input = Entry(width=24)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text='Search', width=15, pady=0, padx=0, command=find_password)
search_button.grid(column=2, row=1)

email_l = Label(text="Email/Username:")
email_l.grid(column=0, row=2)

email_input = Entry(width=24)
email_input.grid(column=1, row=2)
email_input.insert(0, 'hdhdhdxhhs@gmail.com')

password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

password_input = Entry(width=24)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", padx=0, pady=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()