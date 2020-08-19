import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors = ('red', 'green', 'blue', 'yellow')
guapi = input('瓜皮，你的名字是神马？')
for i in range(1000):
    t.pencolor(colors[i % 4])
    t.penup()
    t.fd(i * 4)
    t.pendown()
    t.write(
        guapi,
        font=(
            'FangSong',
            (i + 4) // 4,
            'italic'
        )
    )
    t.left(92)
turtle.mainloop()