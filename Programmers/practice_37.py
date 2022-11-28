#7의 개수
def solution(array):
    answer = 0

    for a in array:
        answer += str(a).count('7')

    return answer


if __name__ == '__main__':
    print(solution([7, 77, 17]))
    print(solution([10, 29]))