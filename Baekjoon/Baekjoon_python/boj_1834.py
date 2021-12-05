#나머지와 몫이 같은 수
import sys
n = int(sys.stdin.readline().rstrip())
total = 0

for i in range(1, n):
    total += (i * n + i)
print(total)