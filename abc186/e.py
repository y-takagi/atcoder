T = int(input())
t = [list(map(int, input().split())) for i in range(T)]


def solve(n, s, k):
    ans = 0
    ps = set()
    ps.add(s)
    while(True):
        d = n - s
        r = d % k
        if r == 0:
            ans += d // k
            print(ans)
            break
        else:
            if d > k:
                s = k - r
            else:
                s = d - r
            if s in ps:
                print(-1)
                break
            ps.add(s)
            ans += d // k + 1


for i in range(T):
    N, S, K = t[i]
    solve(N, S, K)
