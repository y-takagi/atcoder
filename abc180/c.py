N = int(input())

a = []
b = []
i = 1
while True:
    r = N % i
    s = N // i
    if r == 0:
        a.append(i)
        b.append(s)
    if i >= s:
        break
    i += 1
b.reverse()

ll = list(set(a + b))

for i in range(len(ll)):
    print(ll[i])
