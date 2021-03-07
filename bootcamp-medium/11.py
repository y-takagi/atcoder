N, M = list(map(int, input().split()))
P = [list(map(int, input().split())) for i in range(N)]
C = [list(map(int, input().split())) for i in range(M)]

for i in range(N):
    a = P[i][0]
    b = P[i][1]

    mi = float('inf')
    ans = 0
    for j in range(M):
        c = C[j][0]
        d = C[j][1]
        m = abs(a - c) + abs(b - d)
        if mi > m:
            mi = m
            ans = j
    print(ans + 1)
