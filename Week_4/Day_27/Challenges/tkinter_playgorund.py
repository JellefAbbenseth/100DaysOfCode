import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


# Button

def button_clicked():
    new_text = input.get()
    print("I got clicked")
    my_label.config(text=new_text)


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tk.Entry(width=10)
input.pack()


window.mainloop()
