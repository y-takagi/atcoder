import math

N = int(input())
X = list(map(int, input().split()))


m = 0
u = 0
t = 0

for i in range(len(X)):
    v = abs(X[i])
    m += v
    u += v ** 2
    if i == 0 or t < v:
        t = v

print(m)
print(math.sqrt(u))
print(t)
