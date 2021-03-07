import math

N = int(input())

def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if N == 1:
    print(0)
elif N == 2:
    print(2)
else:
    ans = combination(N, N - 2) * (10 ** (N - 2))
    print(ans % (10 ** 9 + 7))
