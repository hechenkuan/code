import turtle
t = turtle.Pen()

t.speed(0)
for x in range(10000):
    t.circle(x*0.1)
    t.left(91)
turtle.mainloop()