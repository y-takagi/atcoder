N = int(input())

s = set()

size = 10 ** 5 + 100

for i in range(2, size):
    for j in range(2, 40):
        t = i ** j
        if t <= N:
            s.add(t)
        else:
            break

print(N - len(s))
