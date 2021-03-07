H, W = list(map(int, input().split()))
a = [list(input()) for i in range(H)]

ri = [False] * 1000
ci = [False] * 1000

for i in range(H):
    if a[i].count('.') == W:
        ri[i] = True

for i in range(W):
    if [a[j][i] for j in range(H)].count('.') == H:
        ci[i] = True

for i in range(H):
    tmp = [a[i][j] for j in range(W) if not ci[j]]
    if tmp.count('.') != len(tmp):
        print(''.join(tmp))
