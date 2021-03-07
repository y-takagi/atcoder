N = int(input())
W = [list(map(int, input().split())) for i in range(N)]

ans = float('inf')

for i in range(N):
    A, B = W[i]
    for j in range(N):
        a, b = W[j]
        if i == j:
            ans = min(ans, A + B)
        else:
            ans = min(ans, max(A, b))

print(ans)
