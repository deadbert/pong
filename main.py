from turtle import Screen
from table import Table
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

pong_table = Table()
paddle_1 = Paddle(paddle='left')
paddle_2 = Paddle(paddle='right')


ball = Ball()

screen.onkey(paddle_1.paddle_up, 'w')
screen.onkey(paddle_1.paddle_down, 's')
screen.onkey(paddle_2.paddle_up, 'Up')
screen.onkey(paddle_2.paddle_down, 'Down')
screen.listen()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    ball.bounce_wall()

    for segment in paddle_2.paddle:
        if segment.distance(ball) < 20:
            ball.bounce_paddle()
    for segment in paddle_1.paddle:
        if segment.distance(ball) < 20:
            ball.bounce_paddle()

    if ball.xcor() > 380:
        pong_table.p2_score += 1
        pong_table.show_score()
        ball.reset_position()

    if ball.xcor() < -380:
        pong_table.p1_score += 1
        pong_table.show_score()
        ball.reset_position()


screen.exitonclick()
