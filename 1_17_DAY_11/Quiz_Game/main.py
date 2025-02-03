from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for que in question_data:
    question_text = que["text"]
    question_answer = que["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_question():
    quiz.next_question()

print(f"completed quiz.your final score{quiz.score}/{quiz.question_no}")
