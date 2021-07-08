#팩토리얼 0의 개수
import sys


def countNum(num, x):
    ans = 0
    while num != 0:
        num = num // x
        ans += num
    return ans


n = int(sys.stdin.readline().rstrip())
print(min(countNum(n, 5), countNum(n, 2)))