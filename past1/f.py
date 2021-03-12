S = input()

words = []
is_processing = False
start = 0

for i in range(len(S)):
    if S[i].isupper():
        if is_processing:
            words.append(S[start:i+1])
            is_processing = False
        else:
            start = i
            is_processing = True

words = sorted(words, key=lambda x: x.lower())
print(*words, sep='')
