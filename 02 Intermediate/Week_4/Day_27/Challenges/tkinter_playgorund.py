import tkinter as tk


def button_clicked():
    new_text = input.get()
    print("I got clicked")
    my_label.config(text=new_text)


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
new_button = tk.Button(text="Nothing")
new_button.grid(column=2, row=0)

button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = tk.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
