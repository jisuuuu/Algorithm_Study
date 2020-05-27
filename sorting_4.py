#최소값 만들기
def solution(A, B):
    answer = 0

    if max(A) < max(B):
        B.sort(reverse=True)
        A.sort()

    else:
        A.sort(reverse=True)
        B.sort()

    for i in range(0, len(B)):
        answer += A[i] * B[i]

    return answer