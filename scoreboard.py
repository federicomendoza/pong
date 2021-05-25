from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score_p1 = 0
        self.current_score_p2 = 0
        self.message = "score: "
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.build_message()

    def build_message(self):
        self.write(self.message + str(self.current_score_p1)+" - "+str(self.current_score_p2), False, ALIGNMENT, FONT)

    def update_score_p1(self):
        self.clear()
        self.current_score_p1 += 1
        self.build_message()

    def update_score_p2(self):
        self.clear()
        self.current_score_p2 += 1
        self.build_message()

    def game_over(self, player):
        self.goto(x=0, y=0)
        self.color("blue")
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        self.goto(x=0, y=-20)
        self.write(f"{player} wins!", False, ALIGNMENT, FONT)

    def restart(self):
        self.goto(x=0, y=-50)
        self.color("blue")
        self.write("press SPACE to RESTART", False, ALIGNMENT, FONT)
        self.goto(x=0, y=-70)
        self.write("CLICK screen to EXIT", False, ALIGNMENT, FONT)