A, B, C = map(int, input().split())
K = int(input())


# C > B > A
for i in range(K):
    if C >= A and A >= B:
        # C >= A >= B
        B = B * 2
    else:
        C = C * 2

if C > B and B > A:
    print("Yes")
else:
    print("No")
