S = list(input())

ans = [0] * (len(S) + 1)

for i in range(len(S)):
    if S[i] == '<':
        ans[i + 1] = max(ans[i + 1], ans[i] + 1)

ans.reverse()
S.reverse()
for i in range(len(S)):
    if S[i] == '>':
        ans[i + 1] = max(ans[i + 1], ans[i] + 1)

print(sum(ans))
