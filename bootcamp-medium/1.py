N = int(input())
a = [int(input()) for i in range(N)]

size = N * 2 + 10

ans = 1
for i in range(size):
    ans = a[ans - 1]
    if ans == 2:
        print(i+1)
        exit()

print(-1)
