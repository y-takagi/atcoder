N = int(input())

def div(n, cnt):
    if n % 2 != 0:
        return cnt
    else:
        return div(n/2, cnt+1)


cnt = 0
ans = 0
for i in range(1, N+1):
    c = div(i, 0)
    if c >= cnt:
        cnt = c
        ans = i

print(ans)
