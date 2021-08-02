def solution(A, K):
    # write your code in Python 3.6
    S = [0 for _ in range(len(A))]

    for i in range(len(A)):
        S[(i + K) % len(A)] = A[i] #K를 더하고 나머지를 구해서 간결하게 하는 방법

    return S