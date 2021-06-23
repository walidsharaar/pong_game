from turtle import  Turtle

class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move =10
        self.y_move=10

    def move(self):
        x_cordinate = self.xcor()+self.x_move
        y_cordinate = self.ycor()+self.y_move
        self.goto(x_cordinate,y_cordinate)

    def bounce_Y_ball(self):
        self.y_cordinate *= -1

    def bounce_x_ball(self):
        self.x_cordinate *= -1




