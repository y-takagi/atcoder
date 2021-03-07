import math

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.append(N+1)

ans = 0

if M == 0:
    ans = 1
elif N == M:
    ans = 0
else:
    A = sorted(A)
    t = []
    ds = float('inf')
    for i in range(M+1):
        d = A[0] if i == 0 else A[i] - A[i-1]
        if d - 1 == 0:
            continue

        ds = min(ds, d - 1)
        t.append(d - 1)

    for i in range(len(t)):
        ans += math.ceil(t[i] / ds)

print(ans)
