#폰 노이만
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    n, d, a, b, f = map(float, sys.stdin.readline().rstrip().split())
    t = d / (a + b) * f
    print('%d %.6f' %(n, t))