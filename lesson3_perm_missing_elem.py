#PermMissingElem
def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    else:
        return len(A) + 1


def solution2(A):# 다른 사람 코드
  return sum (range(len(A)+2)) - sum(A)