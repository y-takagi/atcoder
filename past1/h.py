from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))
Q = int(input())
S = [list(map(int, input().split())) for i in range(Q)]

s1 = defaultdict(int)
s2 = 0
s3 = 0
s2_min = float('inf')
s3_min = float('inf')

for i in range(N):
    if i % 2 == 0:
        s2_min = min(s2_min, C[i])
    s3_min = min(s3_min, C[i])

for i in range(Q):
    s, x, n = 0, 0, 0
    if len(S[i]) == 3:
        s, x, n = S[i]
        x -= 1
    else:
        s, n = S[i]

    if s == 1:
        if x % 2 == 0:
            c = C[x] - (s1[x] + s2 + s3 + n)
            if c >= 0:
                s1[x] += n
                s2_min = min(s2_min, c)
                s3_min = min(s3_min, c)
        else:
            c = C[x] - (s1[x] + s3 + n)
            if c >= 0:
                s1[x] += n
                s3_min = min(s3_min, c)
    elif s == 2:
        if s2_min >= n:
            s2_min -= n
            s2 += n
            s3_min = min(s3_min, s2_min)
    else:
        if s3_min >= n:
            s3_min -= n
            s3 += n
            s2_min -= n

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += s1[i] + s2 + s3
    else:
        ans += s1[i] + s3

print(ans)
