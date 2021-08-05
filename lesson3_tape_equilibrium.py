# TapeEquilibrium
def solution(A):
    # write your code in Python 3.6
    min_num = None
    sum1 = 0
    sum2 = sum(A)

    for i in range(len(A) - 1):
        sum1 += A[i]
        sum2 -= A[i]
        res = abs(sum1 - sum2)

        if min_num is None or res < min_num:
            min_num = res

    return min_num