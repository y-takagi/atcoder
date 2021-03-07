N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for i in range(N)]

v_max = 10 ** 5 + 100

dp = [[float('inf')] * (v_max + 1) for i in range(N + 1)]
dp[0][0] = 0


def weight(i):
    return wv[i][0]


def value(i):
    return wv[i][1]


for i in range(N):
    for j in range(v_max):
        if j - value(i) >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - value(i)] + weight(i))
        else:
            dp[i + 1][j] = dp[i][j]

ans = 0
for j in range(v_max):
    if dp[-1][j] <= W:
        ans = j
print(ans)
