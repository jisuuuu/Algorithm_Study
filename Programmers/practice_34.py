#잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []

    while len(my_str) > n:
        answer.append(my_str[:n])
        my_str = my_str[n:]
    answer.append(my_str)
    return answer


if __name__ == '__main__':
    print(solution('abc1Addfggg4556b', 6))
    print(solution('abcdef123', 3))