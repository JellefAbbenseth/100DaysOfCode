from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
q_text = "question"
q_answer = "correct_answer"

for data in question_data:
    question_bank.append(Question(data[q_text], data[q_answer]))

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.has_next_question():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
