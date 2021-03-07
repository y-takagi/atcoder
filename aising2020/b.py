N = int(input())
a = list(map(int, input().split()))

count = 0
for i, v in enumerate(a):
    index = i + 1
    if index % 2 != 0 and v % 2 != 0:
        count += 1
print(count)
