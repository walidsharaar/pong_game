from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def go_up(self):
        self.new_y=self.self.ycor()+20
        self.self.goto(self.self.xcor(),self.new_y)

    def go_down(self):
        self.new_y = self.self.ycor() - 20
        self.self.goto(self.self.xcor(), self.new_y)


