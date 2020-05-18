#같은 숫자는 싫어
def solution(arr):
    answer = []
    before = -1

    for a in arr:
        if before != a:
            answer.append(a)
        before = a
    return answer