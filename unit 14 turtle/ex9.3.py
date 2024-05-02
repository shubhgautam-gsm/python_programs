import turtle
# Setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

t = turtle.Turtle()
t1 = turtle.Turtle()
t2= turtle.Turtle()

t.speed(2)
t.color("yellow")
t.width(27)

t1.speed(2)
t1.color("red")
t1.width(27)

t2.speed(2)
t2.color("green")
t2.width(27)

t.circle(100, -80)
t1.penup()
t1.circle(100, -80)
t1.pendown()
t1.circle(100, -120)
t2.circle(100,80)
t2.left(100)
t2.forward(100)






# Hide the turtle
t.hideturtle()

# Keep window open
screen.mainloop()
