
import turtle
turtle.hideturtle()
t = turtle.Pen()
t.pencolor('red')
t.pensize(4)

for i in range(4):
    for j in range(3):
        t.fd(100)
        t.rt(120)
    t.rt(90)

turtle.mainloop()