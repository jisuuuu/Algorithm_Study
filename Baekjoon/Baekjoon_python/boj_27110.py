#특식 배부
import sys
n = int(sys.stdin.readline().rstrip())
a, b, c = map(int, sys.stdin.readline().rstrip().split())
total = min(n, a) + min(n, b) + min(n, c)

print(total)