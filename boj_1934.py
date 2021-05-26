#최소공배수
import sys, math

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a * b // math.gcd(a, b))