# MissingInteger
def solution(A):
    # write your code in Python 3.6
    A.sort()
    min = 1

    for a in A:
        if a == min:
            min += 1

    return min