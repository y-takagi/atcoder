import itertools
from collections import defaultdict

N, M = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(M)]
K = int(input())
P = [list(map(int, input().split())) for i in range(K)]

p = list(itertools.product(*P))

ans = 0

for i in p:
    data = defaultdict(bool)
    for j in i:
        data[j] = True
    tmp = 0
    for s in S:
        a, b = s
        if data[a] and data[b]:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
