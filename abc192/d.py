X = input()
M = int(input())

d = int(max(X)) + 1

alnum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJELMNOPQRSTUVWXYZ"


def nencode(num, chars=alnum):
    s = ""
    while num != 0:
        s = chars[num % len(chars)] + s
        num = num - num % len(chars)
        num = num / len(chars)
    return s


def ndecode(s, chars=alnum):
    num = 0
    for char in s:
        num = num * len(chars)
        num = num + chars.index(char)
    return num


ans = set()
for i in range(d, 63):
    tmp = ndecode(X, alnum[0:i])
    if tmp <= M:
        ans.add(tmp)

print(len(ans))
