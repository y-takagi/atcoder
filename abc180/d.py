X, Y, A, B = list(map(int, input().split()))

e = 0

while True:
    v1 = X * A
    v2 = X + B
    if v1 < v2:
        X = v1
    else:
        X = v2

    if Y > X:
        e += 1
    else:
        break

print(e)
