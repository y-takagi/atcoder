import math

N, D = map(int, input().split())

X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


count = 0
for i in range(N):
    d = math.sqrt(X[i] ** 2 + Y[i] ** 2)
    if D >= d:
        count += 1
print(count)
