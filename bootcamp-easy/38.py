T = [int(input()) for i in range(5)]

TT = [0] * 5

for i in range(5):
    TT[i] = int((T[i] + 9) / 10) * 10

ans = float('inf')
for i in range(5):
    s = 0
    for j in range(5):
        if i == j:
            s += T[i]
        else:
            s += TT[j]
    ans = min(ans, s)

print(ans)
