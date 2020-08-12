import turtle

# # 循环指定的次数
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# turtle.mainloop()


for i, a in enumerate([1+1, 2-1, 4*4, 100/4, 1]):
    # 如果是单数行，输出 <<<<<<<<<<，否则输出 >>>>>>>>>>>>>>>>>
    print(f'i 的值是 {i}, a 的值是 {a}')

da = 99
if da > 100:
    print('you are old')
elif da > 80:
    print('you not clever')
else:
    print('you are stupid')

if a is None:
    print(a)
np = 0
while np < 1:
    np += 1
    print(np)

for x in range(0, 20):
    print('hello %s' % x)
    if x <9: 
        break

吾的年龄 = 0
while 吾的年龄 < 10:
    吾的年龄 += 2
    print(吾的年龄)
yegg =0
xxx =['西瓜','肥宅快乐水','大嘴巴子','汤','米饭']
for i in xxx:
    yegg +=1
    print(yegg,i)

    


    
xxx =['西瓜','肥宅快乐水','大嘴巴子','汤','米饭']

for i, x in enumerate(xxx):
    print(i+1, x)




i = 1000
for x in range(15):
    i +=1
    print(i * 0.165)