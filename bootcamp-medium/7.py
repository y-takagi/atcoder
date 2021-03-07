N = int(input())
S = input()

ans = 0

for i in range(1, N):
    s = set(S[0:i])
    r = set(S[i:N])

    cnt = 0
    for j in r:
        if j in s:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
