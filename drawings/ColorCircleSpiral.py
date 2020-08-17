import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
colors=("red","blue","green","yellow")
for x in range(10000):
    t.pencolor(colors[x % 4])
    t.circle(x*0.1)
    t.left(91)
turtle.mainloop()