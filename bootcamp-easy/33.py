import re

A, B = list(map(int, input().split()))
S = input()

m = re.fullmatch('[0-9]{{{}}}-[0-9]{{{}}}'.format(A, B), S)

if m is None:
    print('No')
else:
    print('Yes')
