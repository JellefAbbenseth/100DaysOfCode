import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
TEXT_SIZE = 15
FONT = (FONT_NAME, TEXT_SIZE)
JUSTIFY_INPUT = "left"
JUSTIFY_LABEL: str = "center"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
name_input.insert(0, "test@mail.com")

pw_input = tk.Entry(width=25, justify=JUSTIFY_INPUT)
pw_input.grid(column=1, row=3)

# Buttons
generate_pw_button = tk.Button(text="Generate Password")
generate_pw_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=40)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
