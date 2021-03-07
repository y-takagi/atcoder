n = int(input())

h = {}


def calc(x, y, z):
    return x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x


for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            a = calc(x, y, z)
            if a not in h:
                h[a] = 1
            else:
                h[a] += 1

for i in range(1, n + 1):
    if i not in h:
        print(0)
    else:
        print(h[i])
