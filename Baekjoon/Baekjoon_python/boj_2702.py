#초6 수학
import sys
import math
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a * b // math.gcd(a, b), math.gcd(a, b))