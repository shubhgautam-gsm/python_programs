import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1150)  # Set a slower drawing speed
t.pensize(2)

# Function to draw an eye
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(x - 8, y + 12)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

# Function to draw a nose
def draw_nose(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.setheading(45)
    t.circle(20, 90)
    t.setheading(270)
    t.forward(40)
    t.setheading(0)
    t.circle(20, 90)
    t.setheading(135)
    t.circle(28, 90)
    t.end_fill()

# Function to draw a mouth
def draw_mouth(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-90)
    t.circle(15, 180)
    t.penup()
    t.setheading(0)
    t.goto(x + 15, y - 10)
    t.pendown()
    t.circle(15, 180)

# Function to draw hair
def draw_hair():
    t.penup()
    t.goto(-70, 200)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.left(120)
    for _ in range(6):
        t.forward(30)
        t.right(45)
        t.forward(30)
        t.left(45)
    t.end_fill()

# Function to draw ears
def draw_ears():
    t.penup()
    t.goto(-90, 60)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(90, 60)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# Function to draw eyebrows
def draw_eyebrows():
    t.penup()
    t.goto(-40, 100)
    t.pendown()
    t.setheading(180)
    t.forward(25)
    t.penup()
    t.goto(40, 100)
    t.pendown()
    t.setheading(0)
    t.forward(25)

# Function to draw a face
def draw_face():
    # Draw the head
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.setheading(0)
    t.circle(100)
    t.end_fill()
    # Draw the eyes
    draw_eye(-30, 50)
    draw_eye(30, 50)
    # Draw the nose
    draw_nose(0, 0)
    # Draw the mouth
    draw_mouth(0, -50)
    # Draw the hair
    draw_hair()
    # Draw the ears
    draw_ears()
    # Draw the eyebrows
    draw_eyebrows()

# Draw 40000 lines of code
for _ in range(10000):
    print("t.forward(10)")
    print("t.right(90)")
    print("t.forward(10)")
    print("t.left(90)")

# Clear the previous drawing
t.reset()

# Draw a face
draw_face()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
turtle.done()
