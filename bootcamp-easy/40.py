a, b = list(map(int, input().split()))

if a <= 0 and b >= 0:
    print('Zero')
elif a > 0 and b > 0:
    print('Positive')
else:
    r = abs(a - b)
    if r % 2 == 0:
        print('Negative')
    else:
        print('Positive')
