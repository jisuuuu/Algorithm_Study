# countDiv
def solution(A, B, K):
    # write your code in Python 3.6
    cnt = 0
    if A % K == 0:
        cnt += 1
    if A != B:
        cnt += int(B / K) - int(A / K)

    return cnt