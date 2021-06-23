from turtle import Turtle
class Paddle:
    def __init__(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.color("white")
        paddle.goto(570, 0)

    def go_up(self):

        self.new_y=self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(),self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)


