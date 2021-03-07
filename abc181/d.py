from collections import Counter as count

def listContains(l1, l2):
    list1 = count(l1)
    list2 = count(l2)
    return list1 & list2 == list1

S = list(input())


ans = False
if len(S) == 1:
    if int(S[0]) % 8 == 0:
        ans = True
elif len(S) == 2:
    if int(S[0] + S[1]) % 8 == 0 or int(S[1] + S[0]) % 8 == 0:
        ans = True
else:
    l = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                a = str(i)
                b = str(j)
                c = str(k)
                if int(a + b + c) % 8 == 0:
                    l.append([a, b, c])

    for i in range(len(l)):
        if listContains(l[i], S):
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")
