N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

L = 0
R = 0
for i in range(M):
    if A[i] < X:
        L += 1
    else:
        R += 1

print(min(L, R))
