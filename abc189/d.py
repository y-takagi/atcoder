N = int(input())
S = [input() for i in range(N)]

t = {1: 1, 0: 1}

for i in range(N):
    s = S[i]

    tmp = {1: 0, 0: 0}
    for j in range(2):
        for k in range(2):
            if s == 'AND':
                tmp[j & k] += t[k]
            else:
                tmp[j | k] += t[k]
    t = tmp

print(t[1])
