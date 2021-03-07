A, B, C = list(map(int, input().split()))

amount = A + B + C

pa = 0
for i in range(100-A):
    pa += (A + i) / (amount + i)

pb = 0
for i in range(100-B):
    pb += (B + i) / (amount + i)

pc = 0
for i in range(100-C):
    pc += (C + i) / (amount + i)

print(pa)
print(pb)
print(pc)

print(pa+pb+pc)
