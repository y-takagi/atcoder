X, K, D = map(int, input().split())

for i in range(K):
    p = X + D
    m = X - D
    if abs(p) < abs(m):
        X = p
    else:
        X = m
print(abs(X))
