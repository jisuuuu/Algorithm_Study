#세균 증식
def solution(n, t):
    answer = n

    for _ in range(t):
        answer *= 2

    return answer


if __name__ == '__main__':
    print(solution(2, 10))
    print(solution(7, 15))