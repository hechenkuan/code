a=set(input('输入字符串'))
b=set(input('再输入字符串'))
# c = a & b
# for i in c:
    # print(i)  

for c in 'abcdefghijklmnopqrstuvwxyz':
    if c in a and c in b:
        print(c)