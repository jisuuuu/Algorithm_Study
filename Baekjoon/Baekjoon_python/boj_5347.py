#LCM
import sys, math

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gcd = math.gcd(a, b)
    print(gcd * (a // gcd) * (b // gcd))