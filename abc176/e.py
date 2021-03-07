H, W, M = map(int, input().split())
C = [list(map(int, input().split())) for i in range(M)]

h = {}
w = {}
for i in range(M):
    hi = C[i][0]
    wi = C[i][1]
    h[hi] = h.get(hi, 0) + 1
    w[wi] = w.get(wi, 0) + 1

ans = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        count = 0
        if [i, j] in C:
            count = h.get(i, 0) + w.get(j, 0) - 1
        else:
            count = h.get(i, 0) + w.get(j, 0)
        ans = max(ans, count)

print(ans)
