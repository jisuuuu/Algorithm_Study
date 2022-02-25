#수도요금
import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

x = a * p
if p <= c:
    y = b
else:
    y = b + (p - c) * d

if x < y:
    print(x)
else:
    print(y)