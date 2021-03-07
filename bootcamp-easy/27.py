N, A, B = list(map(int, input().split()))

ans = min(N%(A+B), A) + (N//(A+B))*A
print(ans)
