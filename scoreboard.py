from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.goto(-100,200)
        self.write(self.left_score ,align="center",font=("Arial",80,"normal"))
    def scoreboard_update(self):


    def left_score(self):
        self.left_score +=1


