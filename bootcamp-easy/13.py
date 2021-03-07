A, B, C = list(map(int, input().split()))

ans = 0
while True:
    if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
        print(ans)
        exit()
    elif A == B == C:
        print(-1)
        exit()
    else:
        a = A / 2
        b = B / 2
        c = C / 2

        A = b + c
        B = a + c
        C = a + b
        ans += 1
