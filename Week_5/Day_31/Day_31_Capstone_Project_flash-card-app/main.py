import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD_PATH = "./images/card_front.png"
BACK_CARD_PATH = "./images/card_back.png"
WRONG_PATH = "./images/wrong.png"
RIGHT_PATH = "./images/right.png"
LANGUAGE_TEXT_FONT = ("Ariel", 40, "italic")
WORD_TEXT_FONT = ("Ariel", 60, "bold")

language = "French"
word = "trouve"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file=FRONT_CARD_PATH)
card_back = tk.PhotoImage(file=BACK_CARD_PATH)
canvas_card.create_image(400, 263, image=card_front)
canvas_language_text = canvas_card.create_text(400, 150, text=language, font=LANGUAGE_TEXT_FONT)
canvas_word_text = canvas_card.create_text(400, 263, text=word, font=WORD_TEXT_FONT)
canvas_card.grid(row=0, column=0, columnspan=2)

canvas_wrong = tk.Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
button_wrong = tk.PhotoImage(file=WRONG_PATH)
canvas_wrong.create_image(50, 50, image=button_wrong)
canvas_wrong.grid(row=1, column=0)

canvas_right = tk.Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
button_right = tk.PhotoImage(file=RIGHT_PATH)
canvas_right.create_image(50, 50, image=button_right)
canvas_right.grid(row=1, column=1)


window.mainloop()
