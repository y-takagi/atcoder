H, W, M = map(int, input().split())
C = [list(map(int, input().split())) for i in range(M)]

h = {}
w = {}
for i in range(M):
    hi = C[i][0]
    wi = C[i][1]
    h[hi] = h.get(hi, 0) + 1
    w[wi] = w.get(wi, 0) + 1

h = sorted(h.items(), key=lambda x:x[1], reverse=True)
w = sorted(w.items(), key=lambda x:x[1], reverse=True)


count = h[0][1] + w[0][1]
if [h[0][0], w[0][0]] in C:
    print(count - 1)
else:
    print(count)
