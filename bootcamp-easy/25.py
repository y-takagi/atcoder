import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

n = list(itertools.permutations(range(1, N + 1)))
a = 0
b = 0

for i in range(len(n)):
    if list(n[i]) == P:
        a = i
    if list(n[i]) == Q:
        b = i

print(abs(a - b))
