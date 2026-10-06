from turtle import Turtle
alignment="center"
fonter=("Arial",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data_snakegame.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align=alignment,font=fonter)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data_snakegame.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()

    def score_counter(self):
        self.score+=1
        self.update_score()

