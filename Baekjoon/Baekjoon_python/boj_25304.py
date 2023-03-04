#영수증
import sys
x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
total = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    total += a * b
print('Yes' if x == total else 'No')