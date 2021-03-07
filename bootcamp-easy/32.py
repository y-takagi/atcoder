N = int(input())
S = input()

x = 0
ans = x
for i in range(N):
    x = x + 1 if S[i] == 'I' else x - 1
    ans = max(ans, x)
print(ans)
