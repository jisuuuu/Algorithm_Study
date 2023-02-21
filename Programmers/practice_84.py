#직사각형 넓이 구하기
def solution(dots):
    x = [d[0] for d in dots]
    y = [d[1] for d in dots]

    return (max(x) - min(x)) * (max(y) - min(y))


if __name__ == '__main__':
    print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
    print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))