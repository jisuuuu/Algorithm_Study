# 약수들의 합
import sys
import math


def get_divisor(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return sorted(list(set(divisors)))


while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    arr = get_divisor(n)
    if n == sum(arr):
        print(n, end=' = ')
        print(' + '.join(list(map(str, arr))))
    else:
        print(f'{n} is NOT perfect.')