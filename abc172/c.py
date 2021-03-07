n, m, k = list(map(int, input().split()))

atimes = list(map(int, input().split()))
btimes = list(map(int, input().split()))

i = 0
j = 0
count = 0
read_time = 0

for i in range(n):
    read_time += atimes[i]
