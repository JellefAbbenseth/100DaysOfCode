from tkinter import messagebox

import tkinter as tk
import random
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
TEXT_SIZE = 15
FONT = (FONT_NAME, TEXT_SIZE)
JUSTIFY_INPUT = "left"
JUSTIFY_LABEL: str = "center"
DEFAULT_NAME = "test@mail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    pw_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    name = name_input.get()
    password = pw_input.get()

    if website == "" or password == "" or name == "":
        tk.messagebox.showwarning(title="Ooops", message="Please don't leave any fields empty!")
        return

    is_ok = tk.messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email/Username: {name}"
                                                             f"\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as pw_file:
            pw_file.write(f"{website} | {name} | {password}\n")
        website_input.delete(0, 'end')
        name_input.delete(0, 'end')
        name_input.insert(0, DEFAULT_NAME)
        pw_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(60, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Bottom area
# Labels
website_label = tk.Label(text="Website: ", font=FONT, justify=JUSTIFY_LABEL)
website_label.grid(column=0, row=1)

name_label = tk.Label(text="Email/Username: ", font=FONT, justify=JUSTIFY_LABEL)
name_label.grid(column=0, row=2)

pw_label = tk.Label(text="Password: ", font=FONT, justify=JUSTIFY_LABEL)
pw_label.grid(column=0, row=3)

# Entries
website_input = tk.Entry(width=40, justify=JUSTIFY_INPUT)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

name_input = tk.Entry(width=40, justify=JUSTIFY_INPUT)
name_input.grid(column=1, row=2, columnspan=2)
name_input.insert(0, DEFAULT_NAME)

pw_input = tk.Entry(width=25, justify=JUSTIFY_INPUT)
pw_input.grid(column=1, row=3)

# Buttons
generate_pw_button = tk.Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
