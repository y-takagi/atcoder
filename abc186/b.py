H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]

amin = float('inf')

for i in range(H):
    for j in range(W):
        amin = min(A[i][j], amin)

ans = 0

for i in range(H):
    for j in range(W):
        ans += A[i][j] - amin

print(ans)
