N = int(input())
D = [list(map(int, input().split())) for i in range(N)]

ans = False
count = 0
for i in range(N):
    if D[i][0] == D[i][1]:
        count += 1
    else:
        count = 0
    if count == 3:
        ans = True

if ans == True:
    print('Yes')
else:
    print('No')
