import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
shadiaoyonghu = int(input('输入1到8'))
colors=("red","blue","green","yellow")
for x in range(1000*shadiaoyonghu):
    t.pencolor(colors[x % 4])
    t.circle(x*0.1)
    t.left(91)
turtle.mainloop()