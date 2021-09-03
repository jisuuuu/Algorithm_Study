#문자열 내림차순으로 배치하기
def solution(s):
    s = list(s)
    s.sort()
    s.reverse()

    return "".join(s)