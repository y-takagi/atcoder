S = input()

ans = float('inf')
for i in range(len(S)-2):
    s = int(S[i:i+3])
    ans = min(ans, abs(753 - s))

print(ans)
