#BABBA
import sys
n = int(sys.stdin.readline().rstrip())
a = [1]
b = [0]

for i in range(n):
    a.append(b[i])
    b.append(b[i] + a[i])
print(f'{a[-1]} {b[-1]}')