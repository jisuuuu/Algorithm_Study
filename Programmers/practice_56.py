# 과일 장수
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        if i + m <= len(score):
            answer += score[i + m - 1]
    answer *= m

    return answer


if __name__ == '__main__':
    print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
    print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))