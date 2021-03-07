N = input()


def rem(s, i):
    return s[:i] + s[i+1:]


i = 0
while True:
    n = len(N)
    r = int(N) % 3
    if r == 0:
        print(i)
        exit()
    elif n == 1:
        print(-1)
        exit()
    elif n == 2:
        for j in range(n):
            s = rem(N, j)
            if int(s) % 3 == 0:
                print(i + 1)
                exit()
        print(-1)
        exit()
    else:
        if r == 1 and ('1' in N or '4' in N or '7' in N):
            print(i + 1)
            exit()
        elif r == 2 and ('2' in N or '5' in N or '8' in N):
            print(i + 1)
            exit()
        else:
            if r == 1:
                k = -1
                for j in ['2', '5', '8']:
                    k = max(N.find(j), k)
                if k > -1:
                    N = rem(N, k)
                else:
                    N = rem(N, 0)
            else:
                k = -1
                for j in ['1', '4', '7']:
                    k = max(N.find(j), k)
                if k > -1:
                    N = rem(N, k)
                else:
                    N = rem(N, 0)

    i += 1
