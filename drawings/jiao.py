#3564
#6 3
n = (input(''))
m = len(n)
b = n[0]
c = n[0]
for i in n:
    if i > b:
        b = i
    if i < c:
        c = i
print(b, c)