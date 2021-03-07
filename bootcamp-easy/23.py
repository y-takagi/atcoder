import math

N = int(input())
D, X = list(map(int, input().split()))
A = [int(input()) for i in range(N)]

ans = X

for i in range(N):
    ans += math.floor((D + A[i] - 1)/A[i])

print(ans)
