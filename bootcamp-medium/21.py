from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))


def comb(n):
    return n * (n - 1) // 2


d = defaultdict(int)

for i in range(N):
    d[A[i]] += 1

amount = 0
for k in d.keys():
    amount += comb(d[k])

for i in range(N):
    a = A[i]
    ans = amount - comb(d[a]) + comb(d[a] - 1)
    print(ans)
