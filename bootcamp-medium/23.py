from collections import defaultdict

N, M = list(map(int, input().split()))
D = [list(map(int, input().split())) for i in range(M)]


def check_input():
    d = defaultdict(lambda: -1)
    for i in range(M):
        s, c = D[i]
        if d[s] != -1 and d[s] != c:
            return False
        else:
            d[s] = c
    if N > 1 and d[1] == 0:
        return False
    return True


if check_input():
    ans = [0] * N
    for i in range(M):
        s, c = D[i]
        ans[s - 1] = c
    if N > 1 and ans[0] == 0:
        ans[0] = 1
    print(*ans, sep=(''))
else:
    print(-1)
