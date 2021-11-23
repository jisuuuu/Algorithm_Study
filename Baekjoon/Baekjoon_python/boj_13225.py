#Divisors
import sys


def get_divisor_cnt(n):
    cnt = 0

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i ==0:
            cnt += 1

            if i != n // i:
                cnt += 1

    return cnt


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(n, get_divisor_cnt(n))