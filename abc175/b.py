from itertools import combinations

N = int(input())
L = list(map(int, input().split()))


def isRectangle(pair):
    if len(pair) < 3:
        return False
    if pair[0] == pair[1] or pair[1] == pair[2] or pair[2] == pair[0]:
        return False
    return (
        pair[0] + pair[1] > pair[2]
        and pair[1] + pair[2] > pair[0]
        and pair[0] + pair[2] > pair[1]
    )


c = list(combinations(L, 3))

count = 0
for i in range(len(c)):
    if isRectangle(c[i]):
        count += 1
print(count)
