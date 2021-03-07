A, B, C = list(map(int, input().split()))

if C == 0:
    if A > B:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if B > A:
        print('Aoki')
    else:
        print('Takahashi')
