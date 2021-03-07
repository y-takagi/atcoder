N = int(input())
A = [int(input()) for i in range(N)]

t = {}

for i in range(N):
    if A[i] in t:
        t[A[i]] = not t[A[i]]
    else:
        t[A[i]] = True

ans = 0
for i in t:
    if t[i]:
        ans += 1

print(ans)
