#JadenCase 문자열 만들기
def solution(s):
    answer = ''
    check = 0

    for idx, r in enumerate(s):
        if idx == 0:
            answer += r.upper()
            continue

        if check == 1:
            answer += r.upper()
        else:
            answer += r.lower()

        if r == ' ':
            check = 1
        else:
            check = 0

    return answer