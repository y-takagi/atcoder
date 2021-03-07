N, x = list(map(int, input().split()))
a = list(map(int, input().split()))

a = sorted(a)

cnt = 0
ans = N - 1
for i in range(N):
    cnt += a[i]
    if cnt == x:
        ans = i + 1
        break
    elif cnt > x:
        ans = i
        break

print(ans)
