N = int(input())
A = list(map(int, input().split()))

m = max(A)

count = 0
ans = 0
for i in range(2, m + 1):
    a = 0
    for j in range(len(A)):
        if A[j] % i == 0:
            a += 1
    if count < a:
        count = a
        ans = i

print(ans)
