import math

s = input()
t = input()

o = 0
for i in range(0, len(t)):
    if s[i] != t[i]:
        o += 1

print(o)
