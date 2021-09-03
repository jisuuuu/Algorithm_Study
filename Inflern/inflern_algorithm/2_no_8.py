#뒤집은 소수
import sys
import math


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))

for a in arr:
    num = reverse(a)
    if isPrime(num):
        print(num, end=' ')
