#거스름돈
import sys
money = [500, 100, 50, 10, 5, 1]
n = 1000 - int(sys.stdin.readline().rstrip())
cnt = 0

for m in money:
    cnt += n // m
    n %= m
print(cnt)