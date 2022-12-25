# 문자열 계산하기
def solution(my_string):
    arr = my_string.split()
    answer = int(arr[0])

    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            answer += int(arr[i + 1])
        else:
            answer -= int(arr[i + 1])

    return answer


if __name__ == '__main__':
    print(solution('3 + 4'))
    print(solution('5 + 7 - 1'))