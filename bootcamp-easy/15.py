N = int(input())
d = list(map(int, input().split()))

d = sorted(d)

b = int(len(d) / 2)
a = b - 1

print(d[b] - d[a])
