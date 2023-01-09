#팩토리얼
import math


def solution(n):
    answer = 1

    while math.factorial(answer) <= n:
        print(f'{n} : {math.factorial(answer)}')
        answer += 1

    return answer - 1


if __name__ == '__main__':
    print(solution(3628800))
    print(solution(7))