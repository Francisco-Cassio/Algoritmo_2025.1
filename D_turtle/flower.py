import turtle

def criar_flor(petalas):
    for i in range(petalas):
        desenhar_petala(flor, 250, 78)
        flor.left(360/petalas)


def desenhar_petala(t, raio, angulo):
    for i in range(2):
        t.circle(raio, angulo)
        t.left(180 - angulo)


flor = turtle.Turtle()
criar_flor(9)
turtle.mainloop()