import random
from turtle import Screen, Turtle


class Paddle:

    def __init__(self):
        self.paddle = Turtle()
        self.paddle.color("orange")
        self.paddle.shape("square")
        self.paddle.shapesize(1,3)
        self.paddle.penup()
        self.paddle.goto(0, -220)
        self.paddle.speed(10)
    def moveleft(self):
        self.paddle.back(10)

    def moveright(self):
        self.paddle.forward(10)


class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.color("purple")
        self.ball.shape("circle")
        self.ball.shapesize(0.5, 0.5)
        self.ball.penup()
        self.ball.goto(random.randrange(-50, 50), -10)
        self.speed = "slow"
        self.move_x = 2
        self.move_y = 2

    def move(self):
        self.new_x = self.ball.xcor() + self.move_x
        self.new_y = self.ball.ycor() + self.move_y
        self.ball.goto(self.new_x, self.new_y)

    def bounce_x(self):
        self.move_x *= -1
        self.move()

    def bounce_y(self):
        self.move_y *= -1
        self.move()
