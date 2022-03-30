#Simple Collatz Sequence
import sys
k = int(sys.stdin.readline().rstrip())
cnt = 0

while k != 1:
    if k % 2 == 0:
        k = k // 2
    else:
        k = k + 1
    cnt += 1
print(cnt)