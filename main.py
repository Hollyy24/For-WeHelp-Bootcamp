from turtle import *
from block import Block
from surround import Paddle, Ball
from scoreboard import Scoreboard
import time


def restart(screen):
    screen.clear()
    screen.title("敲敲樂")
    screen.bgcolor("PINK")
    screen.setup(width=700, height=700)
    screen.tracer(0)

    B = Block()
    P = Paddle()
    b = Ball()
    s = Scoreboard()

    screen.listen()
    screen.onkey(P.moveleft, "Left")
    screen.onkey(P.moveright, "Right")
    screen.onkey(lambda:restart(screen), "space")

    b.ball.goto(0, -200)

    is_on_game = True

    while is_on_game:
        time.sleep(0.01)
        screen.update()
        b.move()
        for block in B.blocks:
            if b.ball.distance(block) <= 30:
                print(f"block")
                s.add_point()
                block.hideturtle()
                B.blocks.remove(block)
                b.bounce_y()
            if b.ball.distance(P.paddle) <= 60:
                screen.update()
                b.bounce_y()
            if b.ball.xcor() < -200 or b.ball.xcor() > 200:
                b.bounce_x()
            if b.ball.ycor() > 200:
                b.bounce_y()

            if b.ball.ycor() < -300:
                screen.reset()
                text = Turtle()
                text.hideturtle()
                text.penup()
                text.color("White")
                text.write("遊戲結束", font=("Arial", 20, "normal"), align="Center")
                text.goto(0, -50)
                text.write("按下空白鍵重新開始", font=("Arial", 20, "normal"), align="Center")
                is_on_game = False
                break


screen = Screen()
restart(screen)
screen.mainloop()


