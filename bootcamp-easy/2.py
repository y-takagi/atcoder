N = int(input())
X = list(map(int, input().split()))

sump = float('inf')
for p in range(1, 101):
    c = 0
    for j in range(N):
        c += (X[j]-p) ** 2
    sump = min(sump, c)

print(sump)
