# 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    sides.sort()

    answer += len([i for i in range(sides[1] - sides[0] + 1, sides[1] + 1)])
    answer += len([i for i in range(sides[1] + 1, sides[0] + sides[1])])

    return answer


if __name__ == '__main__':
    print(solution([1, 2]))
    print(solution([3, 6]))
    print(solution([11, 7]))