import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.bgcolor("black")
screen.setup(width=1200,height=700)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((550,0))
left_paddle = Paddle((-550,0))
ball=Ball()
screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #wall detection
    if ball.ycor()>280 or ball.ycor()<-280:
        # need to bounce
        ball.bouce_ball()








screen.exitonclick()

