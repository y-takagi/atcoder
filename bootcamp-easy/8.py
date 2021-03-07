import math

s = int(''.join(input().split()))

r = math.floor(math.sqrt(s))

if r ** 2 == s:
    print('Yes')
else:
    print('No')
