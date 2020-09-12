sao = float(input('输入一个学生的分数'))
if 0 <= sao < 60:
    print('等级是不及格')
elif sao < 80 and sao >= 60:
    print('等级是及格')
elif sao < 90 and sao >= 80:
    print('等级是良好')
elif sao <= 100 and sao >= 90:
    print('等级是优秀')
else:
    print('请输入正确的数，正确的范围是（0~100）')
