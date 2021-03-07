import itertools

N, K = list(map(int, input().split()))
T = [list(map(int, input().split())) for i in range(N)]

ll = list(itertools.permutations(list(range(1, N))))

ans = 0
for r in ll:
    s = T[r[-1]][0]
    for i in range(len(r)):
        if i == 0:
            s += T[0][r[i]]
        else:
            s += T[r[i - 1]][r[i]]
    if s == K:
        ans += 1
print(ans)
