N = int(input())

count = 0

for a in range(1, N):
    b = N // a
    if N % a == 0:
        b -= 1
    count += b
print(count)
