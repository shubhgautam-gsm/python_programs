import turtle

# Setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Turtle
t = turtle.Turtle()
t1 = turtle.Turtle()


t.speed(11)
t.color("yellow")
t.width(25)
t1.speed(11)
t1.color("blue")
t1.width(10)

# Draw the "G"
t.circle(100,360)
t1.circle(100,360)
t1.penup()
t1.goto(30,100)
t1.pendown()
t1.circle(30,360)
t1.circle(10,360)
t1.penup()
t1.goto(-30,100)
t1.pendown()
t1.circle(30,360)    
t1.circle(10,360)
t1.penup()
t1.goto(-30,30)
t1.pendown()
t1.circle(60,120)

# Hide the turtle
t.hideturtle()

# Keep window open
screen.mainloop()
