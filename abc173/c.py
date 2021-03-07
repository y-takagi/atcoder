import itertools

h, w, k = map(int, input().split())
c = []
for i in range(h):
    c.append(list(input()))

del_row = lambda items, del_indexes: [
    item for index, item in enumerate(items) if index not in del_indexes
]

total = 0

for i in range(h):
    for j in range(w):
        for ic in itertools.combinations(range(h), i):
            for jc in itertools.combinations(range(w), j):
                if k == sum(
                    del_row(c[ii], jc).count("#") for ii in set(ic) ^ set(range(h))
                ):
                    total += 1

print(total)
