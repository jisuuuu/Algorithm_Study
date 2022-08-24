#다각형의 대각선
import sys
n = int(sys.stdin.readline().rstrip())

if n < 4:
    print(0)
else:
    answer = 1
    for i in range(n, n - 4, -1):
        answer *= i
    answer = answer // 24
    print(answer)