import sys


def solution(array, n):
    array.sort()
    answer = sys.maxsize
    idx = 0

    for i, a in enumerate(array):
        if answer > abs(n - a):
            answer = abs(n - a)
            idx = i

    return array[idx]


if __name__ == '__main__':
    print(solution([3, 10, 28], 20))
    print(solution([10, 11, 12], 13))