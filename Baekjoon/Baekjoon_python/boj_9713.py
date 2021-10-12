#Sum of Odd Sequence
import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    print(sum([a for a in range(1, num + 1) if a % 2]))