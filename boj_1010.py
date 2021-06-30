#다리 놓기
import sys


def factorial(x):
    num = 1
    for i in range(1, x + 1):
        num *= i
    return num


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))
