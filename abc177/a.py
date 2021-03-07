int_input = lambda: int(input())
int_inputs = lambda: list(map(int, input().split()))

D, T, S = int_inputs()

if T * S >= D:
    print('Yes')
else:
    print('No')
