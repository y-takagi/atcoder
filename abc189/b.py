N, X = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(N)]

al = 0

for i in range(N):
    v = S[i][0]
    p = S[i][1]

    al += (v * p)
    if al > (100 * X):
        print(i + 1)
        exit()

print(-1)
