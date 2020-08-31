""" 第六页：例题2
用海龟绘图画一个四个圆组成的图形
"""

import turtle
t = turtle.Pen()
t.speed(0)
t.pencolor('red')
for i in range(4):
    t.circle(100)
    t.left(90)

turtle.done()
