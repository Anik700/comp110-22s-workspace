from pickletools import floatnl
from turtle import Turtle, colormode, done
bob: Turtle = Turtle()

bob.penup()
bob.goto(50, 50)
bob.color("yellow","yellow")
bob.pendown()

i: int = 0
while (i < 5):
    bob.forward(200)
    bob.left(144)
    i = i + 1

done()