N = int(input())
A = [int(input()) for i in range(N)]

t = [0] * N

for i in range(N):
    t[A[i] - 1] += 1

x = 0
y = 0
for i in range(N):
    if t[i] == 0:
        x = i + 1
    elif t[i] > 1:
        y = i + 1

if x == 0 and y == 0:
    print('Correct')
else:
    print('{} {}'.format(y, x))
