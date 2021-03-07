N, C = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(N)]

size = 10 ** 9 + 10
t = [0] * size

for i in range(N):
    a, b, c = s[i]
    t[a - 1] += c
    t[b] -= c

for i in range(size - 1):
    t[i+1] += t[i]

ans = 0
for i in range(size):
    ans += min(t[i], C)

print(ans)
