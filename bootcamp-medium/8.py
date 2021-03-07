N = int(input())
a = list(map(int, input().split()))

t = set()
f = 0

for i in a:
    tmp = i // 400
    if tmp > 7:
        f += 1
    else:
        t.add(tmp)

mi = 1 if len(t) == 0 and f != 0 else len(t)
ma = len(t) + f

print('{} {}'.format(mi, ma))
