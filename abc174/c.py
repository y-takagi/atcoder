import math

K = int(input())

count = 0
for i in range(1, 100000):
    a = int("7" * i)
    if count == 0 and a % K == 0:
        count = i
        break

if count == 0:
    print(-1)
else:
    print(count)
