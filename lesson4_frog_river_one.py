#FrogRiverOne
def solution(X, A):
    # write your code in Python 3.6
    check = [0 for _ in range(X)]

    for i, a in enumerate(A):
        if not check[a - 1]:
            check[a - 1] = 1
        if all(check):
            return i
    else:
        return -1
#시간 초과 2개

def solution(X, A):
    # write your code in Python 3.6
    check = set()

    for i, a in enumerate(A):
        check.add(a)

        if len(check) == X:
            return i
    return -1
#너무 간단하뮤ㅠ