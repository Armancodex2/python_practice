import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Slow Heart Spiral")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.color("red")
t.hideturtle()

turtle.tracer(0)

# Draw hearts slowly
for i in range(80):

    t.penup()
    t.goto(0, 0)
    t.pendown()

    t.setheading(i * 4)

    scale = 1 + i * 0.15

    for angle in range(360):

        a = math.radians(angle)

        x = scale * 16 * (math.sin(a) ** 3)
        y = scale * (
            13 * math.cos(a)
            - 5 * math.cos(2 * a)
            - 2 * math.cos(3 * a)
            - math.cos(4 * a)
        )

        t.goto(x * 6, y * 6)

    turtle.update()

    # Slows the animation
    time.sleep(0.08)

turtle.done()
