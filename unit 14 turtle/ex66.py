import turtle
import random

def draw_face():
    # Set up turtle
    turtle.speed(0)  # Set maximum drawing speed
    turtle.width(2)  # Set pen width

    # Draw face
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.fillcolor("peachpuff")
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(100, 180)
        turtle.circle(100/3, 180)
    turtle.end_fill()

    # Draw left eye
    turtle.penup()
    turtle.goto(-40, 50)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draw right eye
    turtle.penup()
    turtle.goto(40, 50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draw left pupil
    turtle.penup()
    turtle.goto(-30, 60)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Draw right pupil
    turtle.penup()
    turtle.goto(50, 60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Draw nose
    turtle.penup()
    turtle.goto(0, 30)
    turtle.pendown()
    turtle.width(4)
    turtle.goto(0, 10)

    # Draw mouth
    turtle.penup()
    turtle.goto(-40, -10)
    turtle.pendown()
    turtle.width(2)
    turtle.right(90)
    turtle.circle(40, 180)
    turtle.penup()

    # Draw hair
    turtle.goto(-100, 120)
    turtle.pendown()
    turtle.width(5)
    turtle.goto(100, 120)
    turtle.penup()

def generate_face():
    turtle.reset()
    draw_face()
    turtle.hideturtle()  # Hide the turtle cursor

def main():
    turtle.setup(width=400, height=400)
    turtle.Screen().bgcolor("lightblue")

    generate_face()

    turtle.done()

if __name__ == "__main__":
    main()
