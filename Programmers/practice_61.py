#k의 개수
def solution(i, j, k):
    answer = 0

    for r in range(i, j + 1):
        answer += str(r).count(str(k))

    return answer


if __name__ == '__main__':
    print(solution(1, 13, 1))
    print(solution(10, 50, 5))
    print(solution(3, 10, 2))