N = int(input())
s = [int(input()) for i in range(N)]

s = sorted(s)
ans = sum(s)

if ans % 10 != 0:
    print(ans)
else:
    for i in range(N):
        if s[i] % 10 != 0:
            ans -= s[i]
            print(ans)
            exit()
    print(0)
