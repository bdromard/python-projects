from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score = {self.score} High Score: {self.high_score}', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # With keyword opens file and closes it when we are done with the program. Executes written-down functions.
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
