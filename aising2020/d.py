N = int(input())
X = int(input(), 2)


def calc2(i):
    if i == 0:
        return 0
    else:
        return i % bin(i).count("1")


f = {}
for i in range(1, N + 1):
    v = X ^ (2 ** ((N - 1) - (i - 1)))
    count = 0
    a = v
    while a != 0:
        if a in f:
            count += f[a]
            break
        else:
            a = calc2(a)
            count += 1
    f[v] = count
    print(count)
