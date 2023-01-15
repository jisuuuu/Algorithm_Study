#유한소수 판별하기
import math


def solution(a, b):
    b //= math.gcd(a, b)

    while b % 2 == 0:
        b //= 2

    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2


if __name__ == '__main__':
    print(solution(7, 20))
    print(solution(11, 22))
    print(solution(12, 21))