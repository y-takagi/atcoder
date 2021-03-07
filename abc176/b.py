N = input()
l = [int(s) for s in list(N)]
ans = sum(l)

if ans % 9 == 0:
    print('Yes')
else:
    print('No')
