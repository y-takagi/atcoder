import math

N, K = list(map(int, input().split()))

n = min(N, K - 1)

ans = 0
for i in range(1, n + 1):
    r = math.ceil(math.log2(K / i))
    ans += (1 / N) * ((1 / 2) ** r)

if n != N:
    ans += (1 / N) * (N - n)

print(ans)
