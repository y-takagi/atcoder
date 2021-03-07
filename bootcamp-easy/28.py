N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    a = [0] * N
    for i in range(N):
        if A[i] % 2 != 0:
            print(cnt)
            exit()
        else:
            a[i] = A[i] / 2
    A = a
    cnt += 1
