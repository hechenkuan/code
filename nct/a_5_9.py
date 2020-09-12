import turtle 
t = turtle.Pen()
t.speed(10)
t.pensize(10)
colors=('green','blue','red','black')
for i in range(4):
    t.pencolor(colors[i])
    t.fd(100)
    t.left(90)
turtle.mainloop()