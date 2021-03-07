sx, sy, gx, gy = list(map(int, input().split()))

a = (sy*gx + gy * sx) / (gy + sy)
print(a)
