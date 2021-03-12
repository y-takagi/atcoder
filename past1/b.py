N = int(input())
A = [int(input()) for i in range(N)]

for i in range(N - 1):
    d = A[i + 1] - A[i]
    if d > 0:
        print('up {}'.format(abs(d)))
    elif d < 0:
        print('down {}'.format(abs(d)))
    else:
        print('stay')
