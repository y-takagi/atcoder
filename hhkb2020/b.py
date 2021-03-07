H, W = list(map(int, input().split()))
S = [input() for i in range(H)]

count = 0

for i in range(H):
    for j in range(W):
        if S[i][j] != '.':
            continue
        if i != H - 1 and S[i + 1][j] == '.':
            count += 1
        if j != W - 1 and S[i][j + 1] == '.':
            count += 1

print(count)
