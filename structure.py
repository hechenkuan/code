print(type(1))
print(type(1.1))
print(type(True))
a = '西瓜'
print(type(a))

# ================
# 列表 - list (可改变)
# ================
a = [12*8, 2/1, True, 1433223, 'ABC']
b = [999//9]
print(a+b)
print(type(a))
print(1 in a)
c = [0]*100
print(c)

print(a[4])

print('diaodaio,dio'[2])

a[2] = 1
print(a)

# v = 'shadiao'
# v[0] = 1  # 对字符串的下标赋值会报错，因为字符串是“不可改变”类型
# print(v)

# 在列表中删除一个元素
del a[2]
print(a)

# 在列表末尾追加一个元素
a.append(666)
print(a)

# 在列表末尾插入多个元素
a.extend(['a', 'b', 'c'])
print(a)

# 在列表中间某个位置插入一个元素
a.insert(2, True)
print(a)

# 在列表末尾弹出一个元素（泡腾片）
x = a.pop()
print(x)
print(a)

print(type(a))


# ================
# 元组 -tuple (不可改变)
# ================

a = (1111*999, 999/1)
print(a)
vvv = (1/1,)*100
print(a+vvv)
print(vvv)

# a[1] = 0.00001 # 元组也是“不可改变”类型，因此不能对其内容赋值
print(a[1])
print(type(a))


# ================
# 集合 - set (可改变) (无序性、唯一性、确定性)
# ================

a = {1111-1111, 8888-678, 0}
print(a)
print(type(a))
b={189189/189,0}
print(b)
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)
a.add(648)
a.update((6,12,24,48,96,192))
print(a)
print(1 in a)