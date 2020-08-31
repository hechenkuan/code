a = int(input())
b = int(input())

# 解法1：交换
if a < b:
    a,b=b,a
print(a-b)

# 解法2：if 语句
# if a>b:
#     print(a-b)
# else:
#     print(b-a)

# 解法3：用 abs 内置函数
print(abs(a-b))
print(a+b)