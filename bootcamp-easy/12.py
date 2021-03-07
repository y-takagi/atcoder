K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

d = A[0] + K - A[-1]
for i in range(N - 1):
    d = max(d, A[i+1] - A[i])

print(K - d)
