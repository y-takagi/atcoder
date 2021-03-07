V, T, S, D = list(map(int, input().split()))

if D >= T*V and D <= S*V:
    print('No')
else:
    print('Yes')
