from turtle import *

# Set parameters.
size=(300, 700)
hideturtle()
bgcolor('black')
pencolor('grey')
dot(10)
fillcolor('grey')
speed(5)
penup()

OUTER_LENGTH = 600
OUTER_WIDTH = 480
INNER_LENGTH = 580
INNER_WIDTH = 460

# Go to top right of outer box.

goto(-200, 300)
pensize(2)
pendown()

# Draw box.
begin_fill()
forward(OUTER_WIDTH)
setheading(270)
forward(OUTER_LENGTH)
setheading(180)
forward(OUTER_WIDTH)
setheading(90)
forward(OUTER_LENGTH)
end_fill()

# DIMENSIONS OF BOX - XY AXIS
# L = OUTER_LENGTH
# W = OUTER_WIDTH
# Left Top corner = -200, 300
# Right Top corner = 200, 300

# Draw outline inside the original flyer.
fillcolor('tan')
pencolor('black')
begin_fill()
showturtle()
penup()
goto(-190, 290)
pendown()
setheading(0)
forward(INNER_WIDTH)
setheading(270)
forward(INNER_LENGTH)
setheading(180)
forward(INNER_WIDTH)
setheading(90)
forward(INNER_LENGTH)
end_fill()
penup()

# Delete later. This is defining 1/4s.
setheading(270)
forward(300) # This brings turtle to half length.
dot(10)
pendown()
setheading(0)
forward(INNER_WIDTH)
dot(10)
setheading(90)
forward(300)
setheading(180)
forward(230)
dot(10)
setheading(270)
forward(INNER_LENGTH)
dot(10)

# Get to the top right of the inner box.
# Comment this out later, too.
setheading(90)
forward(580)
setheading(180)
forward(230)
setheading(0)

# Start writing the outside borders.
























done()