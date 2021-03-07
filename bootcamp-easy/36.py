N, M = list(map(int, input().split()))
C = [list(map(int, input().split())) for i in range(M)]

size = N + 10
t = [0] * size

for i in range(M):
    L = C[i][0]
    R = C[i][1] + 1
    t[L] += 1
    t[R] -= 1

for i in range(size - 1):
    t[i + 1] += t[i]

print(t.count(M))
