#삼각형의 완성조건 (1)
def solution(sides):
    sides = sorted(sides)
    return 1 if sides[2] < sum(sides[:2]) else 2


if __name__ == '__main__':
    print(solution([1, 2, 3]))
    print(solution([3, 6, 2]))
    print(solution([199, 72, 222]))