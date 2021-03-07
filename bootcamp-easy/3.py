N, A, B = list(map(int, input().split()))
S = input()

ok = 0
kaigai = 0
for s in S:
    if s == 'a':
        if ok < A + B:
            ok += 1
            print('Yes')
        else:
            print('No')
    elif s == 'b':
        kaigai += 1
        if ok < A + B and kaigai <= B:
            ok += 1
            print('Yes')
        else:
            print('No')

    else:
        print('No')
