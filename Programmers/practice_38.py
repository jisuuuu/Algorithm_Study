#숫자 찾기
def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k)) + 1
    else:
        return -1


if __name__ == '__main__':
    print(solution(29183, 1))
    print(solution(232443, 4))
    print(solution(123456, 7))