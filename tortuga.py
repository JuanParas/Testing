import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(10)

#Crea el primer triángulo
for x in range(36):
    t.pencolor(colors[x%6])
    t.width(2)
    t.forward(x)
    t.left(120)
t.left(120)

#Loop para crear 5 triángulos más
for xx in range(5):
    for x in range(36):
        t.pencolor(colors[5-(x%6)])
        t.width(2)
        t.forward(35-x)
        t.right(120)
    t.left(60)
    for x in range(36):
        t.pencolor(colors[x%6])
        t.width(2)
        t.forward(x)
        t.left(120)