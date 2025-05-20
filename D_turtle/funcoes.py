import math

def square(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)


def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


def circle(t, r):
    circunferencia = 2 * math.pi * r
    n = int(circunferencia / 3) + 1
    length = circunferencia / n
    polygon(t, n, length)