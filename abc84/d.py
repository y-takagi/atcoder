Q = int(input())
q = [list(map(int, input().split())) for i in range(Q)]

size = 10**5 + 100
prime = [True] * size
prime[0] = False
prime[1] = False
for i in range(2, size):
    if not prime[i]:
        continue
    for j in range(i*2, size, i):
        prime[j] = False

a = [0] * size
for i in range(size):
    if i % 2 == 0:
        continue
    if prime[i] and prime[int((i+1)/2)]:
        a[i] = 1

d = [0] * size
for i in range(size - 1):
    d[i + 1] = d[i] + a[i]

for i in range(Q):
    l = q[i][0]
    r = q[i][1] + 1
    print(d[r] - d[l])

