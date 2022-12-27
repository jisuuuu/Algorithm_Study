#머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0

    for a in array:
        if a > height:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([149, 180, 192, 170], 167))
    print(solution([180, 120, 140], 190))