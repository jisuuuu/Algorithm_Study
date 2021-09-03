#이상한 문자 만들기
def solution(s):
    answer = ''

    new = s.split(' ')

    for n in new:
        for i, t in enumerate(n):
            if i % 2 == 0:
                answer += t.upper()
            else:
                answer += t.lower()
        answer += ' '
    return answer[:-1]