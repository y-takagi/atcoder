import itertools

N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

c = list(itertools.combinations(P, 3))

ans = False
for i in range(len(c)):
    p0 = c[i][0]
    p1 = c[i][1]
    p2 = c[i][2]

    y = 0
    if p0[0] == p1[0]:
        if p2[0] == p0[0]:
            ans = True
            break
    elif p0[1] == p1[1]:
        if p2[1] == p0[1]:
            ans = True
            break
    else:
        y = (((p1[1] - p0[1])/(p1[0] - p0[0])) * (p2[0] - p0[0])) + p0[1]
        if y == p2[1]:
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")
