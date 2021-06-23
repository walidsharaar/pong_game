from turtle import  Turtle

class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("Circle")
        self.color("white")
        self.penup()
    def move(self):
        x_cordinate = self.xcor()+10
        y_cordinate = self.ycor()+10
        self.goto(x_cordinate,y_cordinate)


