import math
H = int(input())

i = 1
ans = i

while True:
    if H == 1:
        break
    else:
        H = math.floor(H/2)
        i = i * 2
        ans += i

print(ans)
