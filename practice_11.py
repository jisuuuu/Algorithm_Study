#소수 찾기
import math


def solution(n):
    check = [True] * (n + 1)
    m = int(math.sqrt(n))

    for i in range(2, m + 1):
        if check[i] == True:
            for j in range(i + i, n + 1, i):
                check[j] = False

    return len([i for i in range(2, n + 1) if check[i] == True])