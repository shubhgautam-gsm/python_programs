import turtle
# Setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")

# Turtle
t0 = turtle.Turtle()
t = turtle.Turtle()
t1 = turtle.Turtle()
t_1 = turtle.Turtle()
t2 = turtle.Turtle()

t.hideturtle()
t0.hideturtle()
t1.hideturtle()
t2.hideturtle()
t_1.hideturtle()

t0.speed(2)
t0.color("red")
t0.width(25)
t.speed(2)
t.color("yellow")
t.width(27)
t2.speed(2)
t2.color("blue")
t2.width(25)
t1.speed(2)
t1.color("green")
t1.width(27)
t_1.speed(2)
t_1.color("green")
t_1.width(27)

# Draw the "G"
t0.circle(100, -200) #(100=radius(size ),-200(forward) opposite'-')
t.circle(100, -80)
t1.circle(100, -40)

t_1.circle(100, 20)
t2.circle(100, 90)
t2.right(90)
t2.backward(110)

# Hide the turtle


# Keep window open
screen.mainloop()
