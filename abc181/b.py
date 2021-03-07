N = int(input())
O = [list(map(int, input().split())) for i in range(N)]

ans = 0
for i in range(N):
    a = O[i][0]
    d = 1
    n = O[i][1] - O[i][0] + 1
    ans += (n * (2*a + n - 1)) / 2
print(int(ans))
