import turtle
window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()
# Set pen color and width
pen.color("blue")
pen.width(3)
# Method 1: Directly begin filling without specifying fill color
pen.begin_fill()
# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.left(90)
# Terminate the filling process
pen.end_fill()
# Move to a new position
pen.penup()
pen.goto(200, 0)
pen.pendown()
# Method 2: Set fill color and then begin filling
pen.fillcolor("yellow")  # Set fill color
pen.begin_fill()         # Begin filling with the specified color
# Draw another square
for _ in range(4):
    pen.forward(100)
    pen.left(90)
# Terminate the filling process
pen.end_fill()
# Finish
turtle.done()
