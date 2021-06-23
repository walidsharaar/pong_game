from turtle import Screen,Turtle
from paddle import Paddle

screen = Screen()
paddle = Paddle()
screen.bgcolor("black")
screen.setup(width=1200,height=700)
screen.title("Pong")
screen.tracer(0)
screen.onkey(paddle.go_up,"Up")
screen.onkey(paddle.go_down,"Down")

game_is_on = True

while game_is_on:
    screen.update()



screen.exitonclick()

