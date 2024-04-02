import turtle

# Setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Turtle
t = turtle.Turtle()
t2 = turtle.Turtle()

t.speed(2)
t.color("red")
t.width(25)
t2.speed(2)
t2.color("blue")
t2.width(25)

# Draw the "G"
t.circle(100, -200)

# Save current position and heading for later
x, y = t.pos()
heading = t.heading()

# Draw the part to be changed to yellow
t.color("yellow")
t.begin_fill()
t.circle(100, 90)
t.left(90)
t.forward(90)
t.end_fill()

# Reset to original position and heading
t.penup()
t.goto(x, y)
t.setheading(heading)
t.pendown()

# Draw the remaining part
t2.circle(100, 90)
t2.left(90)
t2.forward(90)

# Hide the turtles
t.hideturtle()
t2.hideturtle()

# Keep window open
screen.mainloop()
