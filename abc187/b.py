N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        x1 = P[i][0]
        y1 = P[i][1]
        x2 = P[j][0]
        y2 = P[j][1]
        d = (y2 - y1) / (x2 - x1)
        if d >= -1 and d <= 1:
            ans += 1

print(ans)
