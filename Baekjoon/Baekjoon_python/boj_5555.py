#반지
import sys
pattern = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(n):
    ring = sys.stdin.readline().rstrip()
    ring += ring

    if pattern in ring:
        cnt += 1
print(cnt)