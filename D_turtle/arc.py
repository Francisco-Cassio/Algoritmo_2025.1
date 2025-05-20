import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    length = 2 * math.pi * r * angle / 360
    n = int(length / 3) + 1
    step_length = length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


bob = turtle.Turtle()
circle(bob, 50)
turtle.mainloop()