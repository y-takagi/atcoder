N = int(input())
A = list(map(int, input().split()))

count = 0
s = {}

for i in range(N - 1):
    d = (A[i] + s.get(i, 0)) - A[i + 1]
    if d > 0:
        count += d
        s[i+1] = d
print(count)
