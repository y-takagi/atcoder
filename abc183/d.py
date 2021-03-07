N, W = list(map(int, input().split()))
C = [list(map(int, input().split())) for i in range(N)]
size = 2 * 10 ** 5 + 5

T = [0] * size

for i in range(N):
    s = C[i][0]
    t = C[i][1]
    p = C[i][2]

    T[s] += p
    T[t] -= p

for i in range(size - 1):
    T[i + 1] += T[i]

for i in range(size):
    if T[i] > W:
        print("No")
        exit()

print("Yes")
