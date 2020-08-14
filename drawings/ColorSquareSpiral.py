import turtle
t = turtle.Pen()
t.speed(0)
colors=("red","blue","green","yellow")
for x in range(1000):   
    t.pencolor(colors[x % 4])
    t.forward(x)
    t.left(90.01 )
turtle.mainloop()