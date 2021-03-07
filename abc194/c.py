from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))


d = defaultdict(int)

for i in range(N):
    d[A[i]] += 1

keys = list(d.keys())
ans = 0

for i in range(len(keys) - 1):
    for j in range(i, len(keys)):
        ans += (d[keys[i]] * d[keys[j]]) * ((keys[i] - keys[j]) ** 2)
print(ans)
