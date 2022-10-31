import random
import pandas
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORDS_CSV_PATH = "./data/french_words.csv"
WORDS_TO_LEARN_PATH = "./data/words_to_learn.csv"
FRONT_CARD_PATH = "./images/card_front.png"
BACK_CARD_PATH = "./images/card_back.png"
WRONG_PATH = "./images/wrong.png"
RIGHT_PATH = "./images/right.png"
LANGUAGE_TEXT_FONT = ("Ariel", 40, "italic")
WORD_TEXT_FONT = ("Ariel", 60, "bold")

language_one = "French"
language_two = "English"
english_word = ""

# ---------------------------- VOCABULARY ------------------------------- #
# Check if "words_to_learn.csv" exists
try:
    dictionary_dict = {row.French: row.English for (index, row) in pandas.read_csv(WORDS_TO_LEARN_PATH).iterrows()}
except FileNotFoundError:
    dictionary_dict = {row.French: row.English for (index, row) in pandas.read_csv(FRENCH_WORDS_CSV_PATH).iterrows()}

french_word = random.choice(list(dictionary_dict.keys()))


def remove_known_word():
    global french_word
    dictionary_dict.pop(french_word)
    dictionary_df = pandas.DataFrame(dictionary_dict.items(), columns=[language_one, language_two])
    dictionary_df.to_csv(WORDS_TO_LEARN_PATH, index=False)
    new_word()


def new_word():
    global french_word, language_one, flip_timer
    window.after_cancel(flip_timer)
    french_word = random.choice(list(dictionary_dict.keys()))
    change_card(card_front, language_one, french_word, "black")
    flip_timer = window.after(3000, flip_card)


# ---------------------------- CHANGE CARD SIDE ------------------------------- #

def flip_card():
    global english_word, english_word, language_two
    english_word = dictionary_dict[french_word]
    change_card(card_back, language_two, english_word, "white")


def change_card(card_side, language, word, color):
    canvas_card.itemconfig(canvas_image, image=card_side)
    canvas_card.itemconfig(canvas_language_text, text=language, fill=color)
    canvas_card.itemconfig(canvas_word_text, text=word, fill=color)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file=FRONT_CARD_PATH)
card_back = tk.PhotoImage(file=BACK_CARD_PATH)
canvas_image = canvas_card.create_image(400, 263, image=card_front)
canvas_language_text = canvas_card.create_text(400, 150, text=language_one, font=LANGUAGE_TEXT_FONT)
canvas_word_text = canvas_card.create_text(400, 263, text=french_word, font=WORD_TEXT_FONT)
canvas_card.grid(row=0, column=0, columnspan=2)

button_image_wrong = tk.PhotoImage(file=WRONG_PATH)
wrong_button = tk.Button(
    height=100,
    width=100,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    image=button_image_wrong,
    command=new_word
)
wrong_button.grid(row=1, column=0)

button_image_right = tk.PhotoImage(file=RIGHT_PATH)
right_button = tk.Button(
    height=100,
    width=100,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    image=button_image_right,
    command=remove_known_word
)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
window.mainloop()
