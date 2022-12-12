#자릿수 더하기
def solution(n):
    answer = 0

    for num in str(n):
        answer += int(num)
    return answer


if __name__ == '__main__':
    print(solution(1234))
    print(solution(930211))