A, B = list(map(int, input().split()))

m = {0: 0, 1: 1, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 3, 8: 3, 9: 2, 10: 1}

n = 0
d = abs(A - B)

if d >= 10:
    n += (d // 10)
    d = (d % 10)

n += m[d]
print(n)
