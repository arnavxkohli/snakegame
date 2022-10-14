import turtle as t
FONT = ("Courier", 12, "normal")


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscores.txt", "r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.pu()
        self.goto(0, 230)
        self.ht()
        self.game_on = True

    def increase(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)
    
    def writehighscore(self):
        with open("highscores.txt", "w") as f:
            f.write(str(self.high_score))
            
    def update(self):
        self.clear()
        self.score += 1
        self.increase()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def game_over(self):
        self.game_on = False
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)

