import math
from collections import defaultdict

K = int(input())
S = input()
T = input()


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


cards = defaultdict(lambda: K)
for i in S + T:
    if i == '#':
        continue
    cards[int(i)] -= 1

tc = defaultdict(int)
ac = defaultdict(int)
for i in S:
    if i == '#':
        continue
    tc[int(i)] += 1
for i in T:
    if i == '#':
        continue
    ac[int(i)] += 1

win_pair = []

for i in range(1, 10):
    for j in range(1, 10):
        temp = cards.copy()
        temp[i] -= 1
        temp[j] -= 1
        if temp[i] < 0 or temp[j] < 0:
            continue

        tcc = tc.copy()
        acc = ac.copy()

        tcc[i] += 1
        acc[j] += 1

        t = 0
        for k in range(1, 10):
            t += k * (10 ** tcc[k])
        a = 0
        for k in range(1, 10):
            a += k * (10 ** acc[k])

        if t > a:
            win_pair.append([i, j])

game = comb((K * 9) - 8, 2)
win = 0

for p in win_pair:
    t, a = p
    if t == a:
        win += cards[t] // 2
    else:
        win += cards[t] * cards[a]

print(len(win_pair) * 2 / game)
