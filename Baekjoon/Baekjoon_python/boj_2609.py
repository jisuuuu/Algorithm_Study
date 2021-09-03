#최대공약수와 최소공배수
import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())

print(math.gcd(n, m))
print(n * m // math.gcd(n, m))