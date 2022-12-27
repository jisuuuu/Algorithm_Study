#최댓값 만들기 (2)
import sys


def solution(numbers):
    answer = -sys.maxsize

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if answer < numbers[i] * numbers[j]:
                answer = numbers[i] * numbers[j]

    return answer


if __name__ == '__main__':
    print(solution([1, 2, -3, 4, -5]))
    print(solution([0, -31, 24, 10, 1, 9]))
    print(solution([10, 20, 30, 5, 5, 20, 5]	))