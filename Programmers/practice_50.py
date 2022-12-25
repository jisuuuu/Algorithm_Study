#약수 구하기
def solution(n):
    answer = []

    for i in range(1, int(n ** (0.5)) + 1):
        if n % i == 0:
            answer.append(i)
            if i ** 2 != n:
                answer.append(n // i)
    answer.sort()
    return answer


if __name__ == '__main__':
    print(solution(24))
    print(solution(29))