from math import factorial

L = int(input())
ans = factorial(L-1)//factorial(11)//factorial(L-12)
print(ans)
