N = int(input())
A = list(map(int, input().split()))

t = [0] * N
for i in range(N):
    a = A[i]
    t[i] = t[i - 1] + a if i > 0 else a

ans = 0
count = 0
m = -float('inf')

for i in range(N):
    m = max(m, t[i])
    ans = max(ans, count + m)
    count = count + t[i]

print(ans)
