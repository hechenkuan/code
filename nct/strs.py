from time import time
import random

a = time()

while True:
    a = str(random.randint(1, 10000000000))
    if a.find('0000000000') > -1:
        print(a)
        break

print(time()-a)


# a = time()
# for i in range(1, 10**8):
#     pass
# print(time()-a)

