N = int(input())
a = list(map(int, input().split()))

sa = sorted(a, reverse=True)
alice = 0
bob = 0

for i in range(N):
    if i % 2 == 0:
        alice += sa[i]
    else:
        bob += sa[i]

print(alice - bob)
