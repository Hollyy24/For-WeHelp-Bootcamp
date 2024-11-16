from  turtle import *

class  Scoreboard:
    def __init__(self):
        self.score = 0
        self.scorebord = Turtle()
        self.scorebord.penup()
        self.scorebord.hideturtle()
        self.scorebord.color("black")
        self.scorebord.goto(-10,250)
        self.scorebord.write(self.score,font=("Arial",20,"bold"))

    def add_point(self):
        self.score += 1
        self.scorebord.clear()
        self.scorebord.write(self.score,font=("Arial",20,"bold"))


