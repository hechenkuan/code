import turtle
t = turtle.Pen()
t.pensize(10)
t.speed(0)
# n = 2
n = int(input('请输入边数：'))
turtle.bgcolor('black')
colors = ("red", "blue", "yellow", "green", "orange", "purple")
for x in range(5000):
    t.pencolor(colors[x % n])
    t.forward(x)
    t.left(360 / n + 91)
turtle.mainloop()
