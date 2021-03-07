A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]

d = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        for k in b:
            if k == A[i][j]:
                d[i][j] = 1

ans = False
for i in range(3):
    cnt = 0
    for j in range(3):
        if d[i][j] == 1:
            cnt += 1
    if cnt == 3:
        ans = True

for i in range(3):
    cnt = 0
    for j in range(3):
        if d[j][i] == 1:
            cnt += 1
    if cnt == 3:
        ans = True

cnt = 0
for i in range(3):
    if d[i][i] == 1:
        cnt += 1
if cnt == 3:
    ans = True

cnt = 0
for i in reversed(range(3)):
    if d[2 - i][i] == 1:
        cnt += 1
if cnt == 3:
    ans = True

if ans:
    print("Yes")
else:
    print("No")
