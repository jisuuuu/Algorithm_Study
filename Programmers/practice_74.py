#최대값 만들기 (1)
def solution(numbers):
    numbers.sort()
    length = len(numbers)
    return numbers[length - 1] * numbers[length - 2]


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([0, 31, 24, 10, 1, 9]))