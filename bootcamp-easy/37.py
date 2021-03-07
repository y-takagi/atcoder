N, K, Q = list(map(int, input().split()))
A = [int(input()) for i in range(Q)]


t = [0] * N

for i in range(Q):
    t[A[i] - 1] += 1

for i in range(N):
    if Q - t[i] >= K:
        print('No')
    else:
        print('Yes')
