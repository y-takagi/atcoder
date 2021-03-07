N = int(input())
A = list(map(int, input().split()))

length = len(A)
al = A[0:length//2]
ar = A[length//2:length]
al_max = max(al)
ar_max = max(ar)

if al_max > ar_max:
    print(A.index(ar_max) + 1)
else:
    print(A.index(al_max) + 1)
