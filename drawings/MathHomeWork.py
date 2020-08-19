while True:
    problem = input('把你的数学题告诉我')
    if problem == 'qq':
        break
    answer = eval(problem)
    print('这送分题的答案是',answer)

