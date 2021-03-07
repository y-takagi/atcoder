S = input()

size = len(S)

bp = 0
bcnt = 0
for i in range(size):
    if S[i] == 'B':
        bp += i
        bcnt += 1

print(sum(range(size - bcnt, size)) - bp)
