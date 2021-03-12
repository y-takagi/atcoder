import copy

N, Q = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(Q)]

T = [['N'] * N for i in range(N)]

for i in range(Q):
    c, a, *b = S[i]
    if c == 1:
        T[a - 1][b[0] - 1] = 'Y'
    elif c == 2:
        t = copy.deepcopy(T)
        for j in range(N):
            if T[j][a - 1] == 'Y':
                t[a - 1][j] = 'Y'
        T = t
    else:
        t = copy.deepcopy(T)
        for j in range(N):
            if T[a - 1][j] == 'Y':
                for k in range(N):
                    if a - 1 == k:
                        continue
                    if T[j][k] == 'Y':
                        t[a - 1][k] = 'Y'
        T = t

for i in range(N):
    print(*T[i], sep='')
