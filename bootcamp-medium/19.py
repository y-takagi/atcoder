R, G, B, N = list(map(int, input().split()))

size = N + 10
ans = 0
for r in range(size):
    for g in range(size):
        s = N - (r*R + g*G)
        if s >= 0 and s % B == 0:
            ans += 1

print(ans)
