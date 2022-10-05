#쿠폰
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    cost = float(sys.stdin.readline().rstrip())
    print(f'${cost * 0.8:.2f}')