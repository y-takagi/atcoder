N = int(input())
A = [int(input()) for i in range(N)]

a = sorted(A)

for i in range(N):
    if A[i] == a[-1]:
        print(a[-2])
    else:
        print(a[-1])
