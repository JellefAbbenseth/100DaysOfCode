import tkinter as tk

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
TRUE_IMG = "images/true.png"
FALSE_IMG = "images/false.png"

PADY = 20
PADX = 20


class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.question = "Amazon qcquired Twitch in August 2014 for $970 million dollars."
        self.window.config(padx=PADX, pady=PADY, bg=THEME_COLOR)

        label = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        label.grid(row=0, column=1)

        canvas = tk.Canvas(width=300, height=250)
        self.question_text = canvas.create_text(150, 125, text=self.question, font=FONT, fill="black")
        canvas.grid(row=1, column=0, columnspan=2, pady=PADY)

        true_img = tk.PhotoImage(file=TRUE_IMG)
        true_button = tk.Button(image=true_img, highlightthickness=0, command=self.test)
        true_button.grid(row=2, column=0)
        false_img = tk.PhotoImage(file=FALSE_IMG)
        false_button = tk.Button(image=false_img, highlightthickness=0, command=self.test_two)
        false_button.grid(row=2, column=1)
        self.window.mainloop()

    def test(self):
        print("test")

    def test_two(self):
        print("test 2")