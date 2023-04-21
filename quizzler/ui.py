import tkinter
from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

# Class QuizInterface that manages the game's interface.

THEME_COLOR = "#375362"
FONT_CFG = ("Arial", 20, "italic")



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window_config = self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png"
                                      )
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="question", fill=THEME_COLOR, font=FONT_CFG, width=280)
        self.score_text = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.check_answer_true)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.check_answer_false)

        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)
        self.score_text.grid(column=1, row=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def check_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

