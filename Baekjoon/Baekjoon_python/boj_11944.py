#NN
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
print((str(n) * n)[:m])