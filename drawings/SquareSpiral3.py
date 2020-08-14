import turtle
t = turtle.Pen()
t.pencolor(1,0,1)
t.speed(0)
for x in range(1000):
    t.forward(x)
    t.left(90.01 )
turtle.mainloop()