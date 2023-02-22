#짝수는 싫어요
def solution(n):
    answer = [i for i in range(1, n + 1) if i % 2 != 0]
    return answer


if __name__ == '__main__':
    print(solution(10))
    print(solution(15))