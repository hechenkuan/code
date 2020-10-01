def my_min(a):
    c = a[0]
    for i in a:
        if i < c:
            c = i
    return c


def bubble_sort(a):
    for i in range(len(a)):
        g = []
        n = a[0]
        for i, x in enumerate(a[1:]):
            if n > x:
                g.append(x)
            else:
                g.append(n)
                n = x
        g.append(n)
        a = g
    return a

def bubble_sort2(a):
    while True:
        g = []
        n = a[0]
        flag = False
        for i, x in enumerate(a[1:]):
            if n > x:
                g.append(x)
                flag = True
            else:
                g.append(n)
                n = x
        g.append(n)
        a = g
        if not flag:
            break

    return a

if __name__ == '__main__':
    # print(my_min([32434234,354353656,8998098089999,120084,3255,423245234541904972,39387983475,2907529]))
    a = [1,5,3,4,7,8,9,6,2]
    a = bubble_sort(a)
    print(a)
    
   

# 5535
# 6654
# 4853
# 9861
# 3086
# 4438
