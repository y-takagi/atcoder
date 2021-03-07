import math

X, Y, R = list(map(float, input().split()))

left = X - R
leftInt = math.floor(left) if left >= 0 else math.ceil(left)

right = X + R
rightInt = math.floor(right) if right >= 0 else math.ceil(right)

ans = 0
for i in range(leftInt, rightInt + 1):
    if (i == left and Y.is_integer()) or (i == right and Y.is_integer()):
        ans += 1
    else:
        b = R if i == X else math.sqrt(R**2 - (X - i)**2)
        ans += math.floor(Y+b) - math.ceil(Y-b) + 1

print(ans)
