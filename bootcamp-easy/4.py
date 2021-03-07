import math

N = int(input())

for x in range(N+1):
    if math.floor(x*1.08) == N:
        print(x)
        exit()

print(':(')
