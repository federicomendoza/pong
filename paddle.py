from turtle import Turtle

P1_POS_0 = (-350, 0)
P2_POS_0 = (350, 0)
PADDLE_STEP = 15


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.score = 1
        self.shapesize(5, 1)
        if player == "p1":
            self.setposition(P1_POS_0)            
        else:
            self.setposition(P2_POS_0)

    def move_up(self):
        last_y = self.ycor()
        if last_y < 230:
            self.goto(self.xcor(), last_y+PADDLE_STEP)
        else:
            pass

    def move_down(self):
        last_y = self.ycor()
        last_x = self.xcor()
        if last_y > -230:
            self.goto(last_x, last_y-PADDLE_STEP)
        else:
            pass






