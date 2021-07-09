#완전제곱수
import sys
import math
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
num = []

for i in range(m, n + 1):
    root = int(i ** 0.5)
    if i == root ** 2:
        num.append(i) #반례가 있기 때문에

if not num:
    print(-1)
else:
    print(sum(num))
    print(min(num))