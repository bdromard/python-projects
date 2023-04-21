from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import requests as req
import json
from ui import QuizInterface

#Stores the data into an array to make it readable in the interface.
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Instances initialization.
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)



