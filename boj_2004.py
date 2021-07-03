#조합의 0의 개수
import sys


#시간 초과
# def factorial(x):
#     ans = 1
#     for i in range(1, x + 1):
#         ans *= i
#     return ans
#
#
# n, m = map(int, sys.stdin.readline().rstrip().split())
# new = str(factorial(n) // (factorial(n - m) * factorial(m)))
# #print(new)
#
# cnt = 0
# for i in range(len(new) - 1, -1, -1):
#     if new[i] != '0':
#         break
#     cnt += 1
# print(cnt)

# 0이 생기는 경우 2와 5의 곱
def countNum(x, y):
    ans = 0
    while x != 0:
        x = x // y
        ans += x
    return ans


n, m = map(int, sys.stdin.readline().rstrip().split())
print(min(countNum(n, 2) - countNum(m, 2) - countNum(n - m, 2), countNum(n, 5) - countNum(m, 5) - countNum(n - m, 5)))