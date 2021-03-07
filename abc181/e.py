N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
W = list(map(int, input().split()))

ans = float('inf')

for i in range(len(W)):
    h = sorted(H + [W[i]])
    s = 0
    for j in range(0, len(h), 2):
        s += h[j + 1] - h[j]
    ans = min(ans, s)

print(ans)
