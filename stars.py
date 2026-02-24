## Random Stars

import random
import turtle

t = turtle.Turtle()

turtle.bgcolor("black")

t.shape("triangle")
t.speed(5)
t.color("white")
t.hideturtle()

for i in range(300):
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(2, 5)
    t.setposition(x, y)
    t.pendown()
    t.dot(size)


turtle.done()
