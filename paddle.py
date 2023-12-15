from turtle import Turtle

LEFT_PADDLE_START = [(-350, -40), (-350, -20), (-350, 0), (-350, 20), (-350, 40)]
RIGHT_PADDLE_START = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]


class Paddle(Turtle):

    def __init__(self, paddle='left'):
        super().__init__()
        self.color = 'white'
        self.paddle = []
        if paddle == 'left':
            self.make_paddle(LEFT_PADDLE_START)
        elif paddle == 'right':
            self.make_paddle(RIGHT_PADDLE_START)

    def make_paddle(self, location):
        for _ in range(0, 5):
            turtle = Turtle()
            turtle.shape('square')
            turtle.color(self.color)
            turtle.penup()
            turtle.goto(location[_])
            self.paddle.append(turtle)

    def paddle_up(self):
        for segment in self.paddle:
            segment.setheading(90)
            segment.forward(20)

    def paddle_down(self):
        for segment in self.paddle:
            segment.setheading(270)
            segment.forward(20)
