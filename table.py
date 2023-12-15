from turtle import Turtle

SCORE_LOCATION = (0, 240)
ALIGNMENT = 'center'
FONT = ('arial', 40, 'normal')


class Table(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.scoreboard()
        self.table_set_up()

    def scoreboard(self):
        self.goto(SCORE_LOCATION)
        self.write(arg=f"{self.p1_score}      {self.p2_score}", align=ALIGNMENT, font=FONT)

    def table_set_up(self):
        table_maker = self.make_painter()
        table_maker.width(5)
        table_maker.goto(0, -300)
        table_maker.setheading(90)
        while table_maker.ycor() < 300:
            table_maker.pendown()
            table_maker.forward(15)
            table_maker.penup()
            table_maker.forward(15)

    def make_painter(self):
        table_maker = Turtle()
        table_maker.hideturtle()
        table_maker.color('white')
        table_maker.penup()
        return table_maker

    def show_score(self):
        self.clear()
        self.write(arg=f"{self.p1_score}      {self.p2_score}", align=ALIGNMENT, font=FONT)
