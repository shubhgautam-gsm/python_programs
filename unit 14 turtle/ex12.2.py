import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()
pen.speed(1000)
#pen.goto(200, 200)
pen.color("Red")
for x in range(1, 50):
    pen.backward(100)
    pen.left(250)
turtle.done()