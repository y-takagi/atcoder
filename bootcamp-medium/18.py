c = [list(map(int, input().split())) for i in range(3)]

for a1 in range(110):
    for a2 in range(110):
        for a3 in range(110):
            b1 = a1 - c[0][0] == a2 - c[1][0] == a3 - c[2][0]
            b2 = a1 - c[0][1] == a2 - c[1][1] == a3 - c[2][1]
            b3 = a1 - c[0][2] == a2 - c[1][2] == a3 - c[2][2]
            if b1 and b2 and b3:
                print('Yes')
                exit()

print('No')
