from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore_from("data.txt")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.set_highscore_in("data.txt", self.highscore)
        self.score = 0
        self.refresh()

    def get_highscore_from(self, path):
        with open(path) as file:
            return int(file.read())

    def set_highscore_in(self, path, score):
        with open(path, mode="w") as file:
            file.write(f"{score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGN, font=FONT)