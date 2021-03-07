N = int(input())
c = list(input())

index = 0
if N % 2 == 0:
    index = N / 2
else:
    index = N // 2


lcount = c[0 : index + 1].count("W")
print(lcount)
