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

print(a[4])  # 下标运算符

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
b = {189189/189, 0}
print(b)
print(a | b)  # 并集
print(a & b)  # 交集
print(a - b)  # 差集
print(b - a)
print(a ^ b)  # 集合的异或
a.add(648)
a.update((6, 12, 24, 48, 96, 192))
print(a)
print(1 in a)

# ================
# 字典 - dict (可改变) (key-value 键值对)
# ================

# 字典是由多个键值对组成的可改变数据结构，每个键必须是唯一的，每个键对应了一个值
# 不可改变的对象（整数、浮点数、字符串、布尔值、元组）都可以作为字典的键
# 任意类型的元素都可以作为字典的值，没有限制
a = {'a': '1', 'b': '2'}
print(type(a))

a = {1.0: 999, 2.0: 888}
print(a)

b = {'daguapi': '99'}

print(b['daguapi'])
# print(a[3]) # 这样会报错，从字典中用下标运算符获取一个不存在的键，会抛出一个 KeyError 错误
# 用get方法可以达到跟下标运算符一样的效果
print(a.get(1.0))
# 但是如果键不存在，则不会报错，而是返回一个None
print(a.get(3))
# 又或者返回一个指定的默认值
print(a.get(3, 4))

a[999]=0.0
print(a[999])

del a[999]
print(a)

print(1 in a)
# 获取字典中所有的键
print(b.keys())
# 获取字典中所有的值
print(b.values())
# 获取所有的键值对
print(a.items())