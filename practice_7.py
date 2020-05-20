#문자열 다루기 기본
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if ord(i) >= 48 and ord(i) <= 57:
                continue
            else:
                return False
        return True
    else:
        return False


def solution2(s):
    return s.isdigit() and len(s) in (4, 6) #문자열의 숫자 포함되여있는지 여부 판단 함수