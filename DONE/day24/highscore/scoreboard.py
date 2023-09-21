from turtle import Turtle,Screen
ALLIGNMENT="center"
FONT =("Courier",15,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day24\data.txt") as data:
            self.high_score= int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.high_score}",align=ALLIGNMENT,font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open("day24\data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",20,"normal"))