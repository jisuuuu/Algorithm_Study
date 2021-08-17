# Distinct

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0

    A.sort()
    distinct = 1
    for i in range(1, len(A)):
        if A[i - 1] != A[i]:
            distinct += 1

    return distinct