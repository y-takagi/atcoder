n = int(input())
s = [input() for i in range(n)]

result = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for r in s:
    result[r] += 1

for k, v in result.items():
    print(k + " x " + str(v))
