N, S, D = list(map(int, input().split()))
P = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    X, Y = P[i]
    if X >= S or D >= Y:
        continue
    print('Yes')
    exit()

print('No')
