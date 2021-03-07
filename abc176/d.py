H, W = map(int, input().split())
C = list(map(int, input().split()))
D = list(map(int, input().split()))
S = [list(input()) for i in range(H)]


wall = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            wall.append([i + 1, j + 1])

