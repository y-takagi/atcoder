N = int(input())
S = [input() for i in range(N)]

t = {}
for i in range(N):
    s = S[i]
    key = s[1:] if s[0] == '!' else s

    if key in t:
        t[key].add(s)
    else:
        t[key] = set([s])

for k in t:
    cnt = len(t[k])
    if cnt > 1:
        print(k)
        exit()

print('satisfiable')
