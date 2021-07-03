#이항 계수1
import sys


def factorial(x):
    ans = 1
    for i in range(2, x + 1):
        ans *= i
    return ans


n, k = map(int, sys.stdin.readline().split())
print(factorial(n) // (factorial(n - k) * factorial(k)))