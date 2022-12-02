#배열 두배 만들기
def solution(numbers):
    return [n * 2 for n in numbers]


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 2, 100, -99, 1, 2, 3]))