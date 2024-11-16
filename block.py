from turtle import Screen, Turtle
import random


class Block:
    def __init__(self):

        self.color = ["red", "blue", "yellow", "green", "purple"]
        self.blocks = []
        self.start_x = -400
        self.start_y = 280
        for i in range(3):
            self.start_y -= 70
            self.start_x = -280
            for j in range(6):
                self.start_x += 70
                self.block = Turtle()
                self.block.shape("square")
                self.block.shapesize(1, 2)
                self.block.penup()
                self.block.color(random.choice(self.color))
                self.block.goto(self.start_x, self.start_y)
                self.blocks.append(self.block)

