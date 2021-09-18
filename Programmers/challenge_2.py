#약수의 개수와 덧셈
def solve(n):
    cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    return cnt


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if solve(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer