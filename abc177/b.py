n_gram = lambda t, n: [t[i:i+n] for i in range(len(t) - n + 1)]

S = input()
T = input()

t_len = len(T)
count = t_len

s_list = n_gram(S, t_len)

for s in s_list:
    c = 0
    for i in range(len(s)):
        if s[i] != T[i]:
            c += 1
    count = min(count, c)

print(count)
