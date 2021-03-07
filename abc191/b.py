N, X = input().split()
A = input().split()

ans = []

for i in range(int(N)):
    if A[i] != X:
        ans.append(A[i])

print(' '.join(ans))
