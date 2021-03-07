import string

S = input()

t = {}

for s in string.ascii_lowercase:
    t[s] = False

for s in S:
    t[s] = True

for s in string.ascii_lowercase:
    if not t[s]:
        print(s)
        exit()

print('None')
