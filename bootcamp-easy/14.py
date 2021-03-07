N, K = list(map(int, input().split()))

r = N % K
r = min(r, abs(r-K))
print(r)
