N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]

ans = 0
for i in range(N):
    t = C
    for j in range(M):
        t += A[i][j] * B[j]
    if t > 0:
        ans += 1

print(ans)
