#고려대학교에는 공식 와인이 있다.
import sys
c, k, p = map(int, sys.stdin.readline().rstrip().split())
total = 0

for i in range(1, c + 1):
    total += ((i * k) + (p * i * i))
print(total)