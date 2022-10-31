import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
TRUE_IMG = "images/true.png"
FALSE_IMG = "images/false.png"

PAD_Y = 20
PAD_X = 20


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.window.config(padx=PAD_X, pady=PAD_Y, bg=THEME_COLOR)

        self.label = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PAD_Y)

        true_img = tk.PhotoImage(file=TRUE_IMG)
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)
        false_img = tk.PhotoImage(file=FALSE_IMG)
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def check_true(self):
        self.give_feedback("True")

    def check_false(self):
        self.give_feedback("False")

    def give_feedback(self, answer: str):
        if self.quiz.check_answer(answer):
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
