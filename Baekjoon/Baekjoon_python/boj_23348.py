#스트릿 코딩 파이터
import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
max_total = 0

for _ in range(n):
    total = 0
    for _ in range(3):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        total += (x * a + y * b + z * c)

    if max_total < total:
        max_total = total
print(max_total)