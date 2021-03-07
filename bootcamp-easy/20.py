s = int(input())

size = 10**6 + 10
a = [0] * size
t = [False] * size


def f(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1


for i in range(10**6 + 10):
    a[i] = s if i == 0 else f(a[i - 1])

    if t[a[i]]:
        print(i+1)
        exit()
    else:
        t[a[i]] = True
