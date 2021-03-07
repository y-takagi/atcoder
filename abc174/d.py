N = int(input())
c = list(input())

done = False
count = 0

for i in range(N):
    if done:
        break
    if c[i] == "R":
        continue
    else:
        l = c[i + 1 :]
        for j in reversed(range(len(l))):
            if l[j] == "R":
                c[i] = "R"
                c[i + 1 + j] = "W"
                count += 1
                break

print(count)
