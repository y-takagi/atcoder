N = int(input())
P = list(map(int, input().split()))

ans = [0] * N
s = set()

for i in range(N):
    s.add(P[i])
    if i == 0:
        if P[0] == 0:
            ans[0] = 1
        else:
            ans[0] = 0
        print(ans[0])
    else:
        if P[i] == ans[i - 1]:
            j = 1
            while ans[i - 1] + j in s:
                j += 1
            ans[i] = ans[i - 1] + j
        else:
            ans[i] = ans[i - 1]
        print(ans[i])
