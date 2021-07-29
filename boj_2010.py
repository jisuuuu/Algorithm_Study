#플러그
import sys
n = int(sys.stdin.readline().rstrip())
total = sum([int(sys.stdin.readline().rstrip()) for _ in range(n)])
print(total - n + 1)