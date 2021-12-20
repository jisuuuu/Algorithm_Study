#수학적 호기심
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1

    print(cnt)