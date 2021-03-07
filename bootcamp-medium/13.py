N = int(input())
p = [[0, 0, 0]] + [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    t = p[i][0]
    x = p[i][1]
    y = p[i][2]

    t2 = p[i+1][0]
    x2 = p[i+1][1]
    y2 = p[i+1][2]

    d = abs(x - x2) + abs(y - y2)
    dt = t2 - t

    if d > dt or abs(dt - d) % 2 != 0:
        print('No')
        exit()

print('Yes')
