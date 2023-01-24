from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data['results']:
    text = item['question']
    answer = item['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    if quiz.still_has_questions() == False:
        print("You've completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")