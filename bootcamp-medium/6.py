H, W = list(map(int, input().split()))

S = [list(input()) for i in range(H)]

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        cnt = 0
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            if x >= 0 and x < H and y >= 0 and y < W and S[x][y] == '#':
                cnt += 1
        S[i][j] = str(cnt)

    print(''.join(S[i]))
