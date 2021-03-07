N = int(input())
a = list(map(int, input().split()))

size = 10**5 + 100

t = [0] * size

for i in range(N):
    tmp = a[i] + 1
    a1 = tmp - 1
    a2 = tmp + 1

    t[tmp] += 1
    t[a1] += 1
    t[a2] += 1

print(max(t))
