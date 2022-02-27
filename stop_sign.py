import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Move the turtle to the starting point.

turtle.home()
turtle.pu()
turtle.sety(125)
turtle.setx(-40)
turtle.pd()

# Draw the octagon.

turtle.color("red")
turtle.begin_fill()
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.forward(100)
turtle.rt(45)
turtle.end_fill()

# Display 'STOP'

turtle.color("black")
turtle.pu()
turtle.sety(-35)
turtle.setx(-75)
turtle.write("STOP", font=("Arial",50,"normal"))
