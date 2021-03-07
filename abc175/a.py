S = list(input())
count = 0
max_count = 0
for i in range(len(S)):
    a = S[i]
    if a == "R":
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(max_count)
