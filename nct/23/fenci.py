import jieba
f = open('23/abc.txt', encoding='utf8')
a = f.read()
f.close()
print(list(jieba.cut(a)))
