N = int(input())
D = [list(map(int, input().split())) for i in range(N)]


ans = float('inf')
for i in range(N):
    a, p, x = D[i]
    if x - a > 0:
        ans = min(ans, p)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
