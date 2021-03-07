A, B, M = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = [list(map(int, input().split())) for i in range(M)]


ans = min(a) + min(b)

for i in range(M):
    x, y, c = m[i]
    ans = min(a[x-1]+b[y-1] - c, ans)

print(ans)
