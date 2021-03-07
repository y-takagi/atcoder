H, W = list(map(int, input().split()))
s = [list(input()) for i in range(H)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for i in range(H):
    for j in range(W):
        if s[i][j] != '#':
            continue
        ans = False
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x >= 0 and x < H and y >= 0 and y < W and s[x][y] == '#':
                ans = True
        if not ans:
            print('No')
            exit()

print('Yes')
