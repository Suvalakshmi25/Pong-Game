from turtle import Turtle
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,dim):
        super().__init__()
        self.dim=dim
        self.shape("square")
        self.color("white")
        self.shapesize(5,0.5)
        self.penup()
        self.goto(dim)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




