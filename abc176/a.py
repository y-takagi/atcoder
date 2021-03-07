import math

N, X, T = map(int, input().split())

ans = math.ceil(N / X) * T
print(ans)
