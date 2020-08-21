import turtle

# 输入家人的名字，存放在列表中
shadiaomingzi = input('沙雕，你叫什么名字')
haoduishadiao = []
while shadiaomingzi != '':
    haoduishadiao += [shadiaomingzi]
    shadiaomingzi = input('输入其他名字，或者按回车结束')
n = len(haoduishadiao)
# 绘制螺旋线
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors = ('red', 'green', 'blue', 'yellow',
          '#1E90FF', '#7F0000', 'lavender')
for i in range(1000):
    t.pencolor(colors[i % n])
    t.penup()
    t.fd(i * 2)
    t.pendown()
    t.write(
        haoduishadiao[i % n],
        font=(
            'FangSong',
            (i + 4) // 4,
            'italic'
        )
    )
    t.left(370/ n)
turtle.mainloop()
