"""A Poor Man's Starry Night."""

__author__= "730243145"

from turtle import Turtle, colormode, done

def main() -> None:
    """The entrypoint of my scene"""
    #initializing turtle variable
    ertle: Turtle = Turtle()
    ertle.speed(0)
    #background color
    draw_sky(ertle, -500, 400, 300)
    #drawing ground
    draw_ground(ertle, -500, -300, 300)
    #drawing moon
    draw_moon(ertle, 150, 275)
    #drawing stars
    draw_stars(ertle, -300, 300)
    draw_stars(ertle, -100, 250)
    draw_stars(ertle, 0, 300)
    draw_stars(ertle, 300, 250)
    #drawing people
    i: int = 0
    x = 50
    while i < 2:
        draw_people(ertle, x, -200)
        x = x + 80
        i = i + 1
    done()

def draw_ground(bob: Turtle, x: float, y: float, width: float) -> None:
    """Draw a rectangle for the ground of the scene."""
    bob.penup()
    bob.goto(x,y)
    bob.color("green")
    bob.fillcolor("green")
    bob.pendown()

    bob.begin_fill()
    i: int = 0
    
    while i < 4:
        bob.forward(1000)
        bob.right(90)
        i = i + 1
    bob.end_fill()

def draw_sky(bob: Turtle, x: float, y: float, width: float) -> None:
    """Draw a rectangle for the sky."""
    bob.penup()
    bob.goto(x,y)
    bob.color("dark blue")
    bob.fillcolor("dark blue")
    bob.pendown()

    bob.begin_fill()
    i: int = 0
    
    while i < 4:
        bob.forward(1000)
        bob.right(90)
        i = i + 1
    bob.end_fill()


def draw_stars(bob: Turtle, x:float, y:float) -> None:
    """Drawing Stars."""
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    bob.color("yellow")
    bob.fillcolor("yellow")
    bob.begin_fill()
    i: int = 0
    while (i < 5):
        bob.forward(50)
        bob.left(144)
        i = i + 1
    bob.end_fill()

def draw_moon(bob: Turtle, x:float, y:float) -> None:
    """Drawing the Moon.""" 
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    bob.color("yellow")
    bob.fillcolor("yellow")
    bob.begin_fill()
    r = 50
    bob.circle(r)
    bob.end_fill()


"""For drawing the people, I decided to break down their bodies into simpler functions."""
def draw_torso(bob: Turtle, length: float) -> None:
    """Drawing body."""
    bob.left(90)
    bob.down()
    bob.forward(length)
    bob.up()
    bob.back(length)
    bob.left(90)

def draw_legs(bob: Turtle) -> None:
    """Drawing legs."""
    bob.right(90)
    bob.forward(100)
    bob.right(45)
    bob.down()
    bob.forward(30)
    bob.back(30)
    bob.left(90)
    bob.forward(30)
    bob.back(30)
    bob.right(45)
    bob.up()
    bob.back(100)
    bob.left(90)

def draw_arms(bob: Turtle) -> None:
    """Draw arms."""
    bob.right(90)
    bob.forward(25)
    bob.left(90)
    bob.down()
    bob.forward(30)
    bob.back(30)
    bob.left(180)
    bob.forward(30)
    bob.back(30)
    bob.left(90)
    bob.up()
    bob.back(30)
    bob.left(90)

def draw_head(bob: Turtle) ->None:
    """Drawing head"""
    bob.down()
    bob.setheading(180.0)
    for x in range(360):
        bob.forward(.3)
        bob.right(1)
    bob.up()

def draw_people(bob: Turtle, x: float, y: float) -> None:
    bob.penup()
    bob.goto(x, y)
    bob.color("white")
    bob.fillcolor("white")
    bob.begin_fill()
    draw_head(bob)
    draw_torso(bob, 100)
    draw_arms(bob)
    draw_legs(bob)
    bob.end_fill()


if __name__ == "__main__":
    main()




    