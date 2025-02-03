class QuizBrain:
    def __init__(self,q_list):
        self.score=0
        self.q_list=q_list
        self.question_no =0
    def still_question(self):
        return self.question_no < len(self.q_list)
    def next_question(self):
        current_q = self.q_list[self.question_no]
        self.question_no +=1
        user_answer=input(f"Q.{self.question_no}:{current_q.text} (True/False)?")
        self.check_answer(user_answer,current_q.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it!")
            self.score+=1
        else:
            print("incorrect answer!")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_no}.")
        print("\n")
