N = int(input())
Y = [list(map(int, input().split())) for i in range(N)]

ys = sorted(Y, key=lambda x: 2*x[0] + x[1], reverse=True)

asum = 0
for i in range(N):
    asum += ys[i][0]

bsum = 0
for i in range(N):
    a = ys[i][0]
    b = ys[i][1]
    asum -= a
    bsum += (a + b)
    if asum < bsum:
        print(i+1)
        exit()
