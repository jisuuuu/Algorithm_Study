#줄 서는 방법
import math

# (0) 1, 2
# (1) 3, 4
# (2) 5, 6
# 짝수면 나누어 떨어져서 - 1
def solution(n, k):
    answer = []
    real = [i for i in range(1, n + 1)]

    while n != 0:
        temp = math.factorial(n) // n
        idx = k // temp
        k = k % temp

        # 짝수면 나누어 떨어져서 - 1
        if k == 0:
            answer.append(real.pop(idx - 1))
        else:
            answer.append(real.pop(idx))

        n -= 1

    return answer

import itertools

#효율성 꽝
def solution(n, k):
    perm = itertools.permutations([i for i in range(1, n + 1)], n)
    answer = list(map(list, perm))
    return answer[k - 1]