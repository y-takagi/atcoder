X, K, D = map(int, input().split())

if abs(X) >= K * D:
    print(abs(X) - (K * D))
else:
    k = abs(X) // D
    Y = abs(X) % D
    if (K - k) % 2 == 0:
        print(Y)
    else:
        print(abs(Y - D))
