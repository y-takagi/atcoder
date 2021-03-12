N, M = list(map(int, input().split()))
T = [input().split() for i in range(M)]

size = (2 ** N)
dp = [0] + ([float('inf')] * (size - 1))


def conv(s):
    v = ''.join(['1' if x == 'Y' else '0' for x in s])
    return int(v, 2)


for i in range(M):
    for j in range(size):
        S = T[i][0]
        C = int(T[i][1])

        v = j | conv(S)
        dp[v] = min(dp[v], dp[j] + C)

ans = dp[size - 1]
print(ans if ans != float('inf') else -1)
