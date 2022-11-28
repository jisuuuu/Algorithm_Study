#삼총사
from itertools import combinations


def solution(number):
    answer = 0
    new = list(combinations(number, 3))

    for n in new:
        if sum(n) == 0:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([-2, 3, 0, 2, -5]))
    print(solution([-3, -2, -1, 0, 1, 2, 3]))
    print(solution([-1, 1, -1, 1]))