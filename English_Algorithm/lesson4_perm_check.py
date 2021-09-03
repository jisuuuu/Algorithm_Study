# PermCheck
def solution(A):
    # write your code in Python 3.6
    A.sort()
    num = 1
    for a in A:
        if a != num:
            return 0
        num += 1

    return 1