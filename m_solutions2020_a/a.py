X = int(input())

for index, i in enumerate(range(2, 10)):
    min = 200 * i
    max = min + 199
    if X >= min and X <= max:
        print(8 - index)
        break
