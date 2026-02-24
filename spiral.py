import turtle as t
from itertools import cycle

t.bgcolor("black")
t.speed("fast")
t.pensize(4)

colors = cycle( ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'white', 'gray'] )

# defining fucntion
def draw_circle(size, angle, move):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(move)
    draw_circle(size + 5, angle + 1, move + 1)

## calling fucntion
draw_circle(30, 0, 1)

t.done()
