#문자열 나누기
def solution(s):
    answer = 0
    check = ['', 0, 0]  # 지정 문자, 지정 문자 수, 비교 문자 수

    for i in s:
        if check[0] == '':
            check[0] = i
            check[1] += 1
        else:
            if check[0] == i:
                check[1] += 1
            else:
                check[2] += 1

            if check[1] == check[2]:
                answer += 1
                check = ['', 0, 0]

    if check != ['', 0, 0]:
        answer += 1

    return answer


if __name__ == '__main__':
    print(solution("banana"))
    print(solution("abracadabra"))
    print(solution("aaabbaccccabba"))