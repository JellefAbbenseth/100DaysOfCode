import tkinter as tk

# static variables
FONT = ("Arial", 20)


# functions
def calculate():
    new_text = miles_input.get()
    new_text = int(round(int(new_text) * 1.609344, 0))
    kms_label.config(text=new_text)


# window
window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# input
miles_input = tk.Entry(width=10, justify="left")
miles_input.grid(column=1, row=0)

# labels
miles_label = tk.Label(text="Miles", font=FONT, justify="right")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to", font=FONT, justify="left")
equal_label.grid(column=0, row=1, padx=20)

kms_label = tk.Label(text="0", font=FONT, justify="center")
kms_label.grid(column=1, row=1)

km_Label = tk.Label(text="Km", font=FONT, justify="right")
km_Label.grid(column=2, row=1)

# button
calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
