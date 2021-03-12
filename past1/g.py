import itertools

N = int(input())
A = [list(map(int, input().split())) for i in range(N - 1)]

D = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i < j:
            D[i][j] = A[i][j - (i + 1)]
        elif i > j:
            D[i][j] = D[j][i]

ans = -float('inf')

for c in itertools.product([0, 1, 2], repeat=N):
    temp = 0
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            if c[i] == c[j]:
                temp += D[i][j]
    ans = max(ans, temp)

print(ans)
