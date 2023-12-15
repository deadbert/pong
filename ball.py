from turtle import Turtle
import random

BALL_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(.65)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(35)
        self.x_vel = 10
        self.y_vel = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_vel
        new_y = self.ycor() + self.y_vel
        self.goto(new_x, new_y)

    def bounce_paddle(self):
        self.x_vel *= -1
        self.y_vel = random.randint(-10, 10)
        self.move_speed *= 0.9

    def bounce_wall(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_vel *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.move_speed = 0.1
