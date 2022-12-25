# 제곱수 판별하기
def solution(n):
    return 1 if int(n ** 0.5) == n ** 0.5 else 2


if __name__ == '__main__':
    print(solution(144))
    print(solution(976))