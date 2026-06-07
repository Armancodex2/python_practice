import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(200):
    t.pencolor(colors[i % 6])
    t.circle(100)
    t.left(10)

turtle.done()
