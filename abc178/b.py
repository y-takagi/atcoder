a, b, c, d = map(int, input().split())

ans = a * c
ans = max(a * d, ans)
ans = max(b * c, ans)
ans = max(b * d, ans)

print(ans)

