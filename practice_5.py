#문자열 내 p와 y의 개수
def solution(s):
    p_count = s.count('p')
    p_count += s.count('P')

    y_count = s.count('y')
    y_count += s.count('Y')

    return True if p_count == y_count else False