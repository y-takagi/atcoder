import math

X = int(input())

while True:
    n = math.floor(math.sqrt(X))
    prime = True
    for i in range(2, n+1):
        if X % i == 0:
            prime = False
            break
    if prime:
        print(X)
        exit()
    X += 1
