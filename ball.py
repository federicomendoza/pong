from turtle import Turtle
import random

BALL_SPEED_INIT = 20
INIT_ANGLE = random.randint(0, 360)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_speed = BALL_SPEED_INIT
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(INIT_ANGLE)
        self.last_direction = self.heading()

    def move(self):
        if 395 > self.xcor() > -395:
            self.setheading(self.last_direction)
            self.forward(self.ball_speed)
            self.wall_collision()
        else:
            pass

        self.last_direction = self.heading()

    def wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(360 - self.last_direction)

    def bounce(self):
        self.setheading(180 - self.last_direction)
        self.last_direction = self.heading()
        self.ball_speed += 5

    def bounce_edge(self, angle):
        self.setheading(180 - angle)
        self.last_direction = self.heading()
        self.ball_speed += 5

    def reset_pos(self):
        self.home()
        self.setheading(INIT_ANGLE)
        self.ball_speed = BALL_SPEED_INIT
