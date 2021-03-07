N, M, T = list(map(int, input().split()))
t = [list(map(int, input().split())) for i in range(M)]

n = N
for i in range(M):
    A = t[i][0]
    B = t[i][1]
    d = A if i == 0 else A - t[i-1][1]
    n = n - d
    if n <= 0:
        print('No')
        exit()
    n = min(n + (B - A), N)

n = n - (T - B)

if n > 0:
    print('Yes')
else:
    print('No')
