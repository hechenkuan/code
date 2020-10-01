a=int(input('输入一个正整数'))
n = 0 
j = 1
while True:
    n=n+1
    j=j+1
    if n*j==a:
        print(n)
        break
    elif n*j>a:
        print(0)
        break
    

