N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for i in range(N)]

dp = [[0] * (W + 1)] + [0] * N


def wi(i):
    return wv[i - 1][0]


def vi(i):
    return wv[i - 1][1]


def value(i, w):
    if w - wi(i) >= 0:
        return max(dp[i - 1][w], dp[i - 1][w - wi(i)] + vi(i))
    else:
        return dp[i - 1][w]


for i in range(1, N + 1):
    dp[i] = [value(i, w) for w in range(W + 1)]

print(dp[-1][-1])
