S = input()


while(True):
    S = S[0:len(S)-1]
    size = len(S)

    if size % 2 == 0 and S[0:int(size/2)] == S[int(size/2):size]:
        print(size)
        exit()
