#3n + 1 수열
import sys
n = int(sys.stdin.readline().rstrip())
cnt = 1
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    cnt += 1
print(cnt)