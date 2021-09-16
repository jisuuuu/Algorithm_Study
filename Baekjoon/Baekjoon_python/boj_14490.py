#백대일
import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split(':'))
print(f'{n // math.gcd(n, m)}:{m // math.gcd(n, m)}')