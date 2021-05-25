from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def play_pong():
    screen = Screen()
    screen.clear()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("PONG")
    screen.tracer(0)

    paddle_p1 = Paddle("p1")
    paddle_p2 = Paddle("p2")
    ball = Ball()
    scoreboard = Scoreboard()
    ball_speed = 0.08

    def paddle_collision(ball, paddle1, paddle2):
        # detect collision with paddles
        if ball.xcor() > 330 and 30 < ball.distance(paddle2) < 50:
            ball.bounce_edge(45)
        elif ball.xcor() > 330 and ball.distance(paddle2) <= 30:
            ball.bounce()
        if ball.xcor() < -330 and 30 < ball.distance(paddle1) < 50:
            ball.bounce_edge(-135)
        elif ball.xcor() < -330 and ball.distance(paddle1) <= 30:
            ball.bounce()

    screen.listen()
    screen.onkeypress(paddle_p1.move_up, "w")
    screen.onkeypress(paddle_p1.move_down, "s")
    screen.onkeypress(paddle_p2.move_up, "Up")
    screen.onkeypress(paddle_p2.move_down, "Down")
    game_on = True

    while game_on:
        time.sleep(ball_speed)
        screen.update()
        ball.move()
        paddle_collision(ball, paddle_p1, paddle_p2)
        if ball.xcor() < -395:
            ball.reset_pos()
            scoreboard.update_score_p2()
        if ball.xcor() > 395:
            ball.reset_pos()
            scoreboard.update_score_p1()
        if scoreboard.current_score_p1 == 5 or scoreboard.current_score_p2 == 5:
            if scoreboard.current_score_p1 > scoreboard.current_score_p2:
                scoreboard.game_over("player 1")
            else:
                scoreboard.game_over("player 2")
            scoreboard.restart()
            screen.onkey(play_pong, "space")
            game_on = False

    screen.exitonclick()

play_pong()