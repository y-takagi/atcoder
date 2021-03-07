N = int(input())
abc = [list(map(int, input().split())) for i in range(N)]

dp = [abc[0]] + [[0, 0, 0] for i in range(N - 1)]

for i in range(1, N):
    for j in range(3):
        dp[i][j] = abc[i][j] + max([dp[i - 1][k] for k in filter(lambda x: x != j, range(3))])

print(max(dp[N - 1]))
