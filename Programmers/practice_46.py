#가장 큰 수 찾기
def solution(array):
    return [max(array), array.index(max(array))]


if __name__ == '__main__':
    print(solution([1, 8, 3]))
    print(solution([9, 10, 11, 8]))