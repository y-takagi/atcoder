A, B, C = list(map(int, input().split()))

ans = 'NO'
for i in range(100000):
    if (B * i + C) % A == 0:
        ans = 'YES'
        break

print(ans)
