import turtle
t = turtle.Pen()
t.speed(0)
t.pensize(2)
turtle.bgcolor('black')
shadiao = int(turtle.numinput('沙雕，输入数字', '填你想的数', 0))
for i in range(shadiao):
    t.pencolor('white')
    t.circle(50)
    t.left(360 / shadiao)
for i in range(shadiao):
    t.pencolor('blue')
    t.circle(100)
    t.left(360/shadiao)
turtle.mainloop()
