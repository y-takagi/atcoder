x, y = list(map(int, input().split()))

ans = abs(x - y)

if ans >= 3:
    print('No')
else:
    print('Yes')
