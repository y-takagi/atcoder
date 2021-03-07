S = input()

for i in range(len(S)):
    for j in range(i, len(S)):
        s = S[0:i] + S[j:len(S)]
        if s == 'keyence':
            print('YES')
            exit()

print('NO')
