#Time to Decompress
import sys
l = int(sys.stdin.readline().rstrip())

for _ in range(l):
    n, x = sys.stdin.readline().rstrip().split()
    print(x * int(n))