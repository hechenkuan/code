"""  运算符

数值运算：+ - * / // % **
比较运算：== != > < >= <=
布尔运算：and or not
赋值运算符：=

字符串支持的运算：+（拼接） *（重复） 比较运算符

优先级

第一层：**
第二层：* / // %
第三层：+ -
第四层：== != > < >= <=
第五层：not
第六层：and 
第七层：or
第八层：=
"""

print(1+3)

print(9999-99999)

print(666*666)

print(12345/3)  # 注意： 1. 不能除零 2. 返回一个浮点值，无论是否能整除

print(100//7)  # 返回带余数除法得到的商（只返回商，不返回余数）

print(100 % 7)  # 返回带余数除法得到的余数（模运算）

print(25**0.5)

print(2 == 8/4)  # True

print(0.3 == 0.1*3)  # False 浮点误差

print(1 < 3 and 4 % 2 == 0)

a='abc'
b='def'
print(a+b)

print(a*3)