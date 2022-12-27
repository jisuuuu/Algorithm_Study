#문자열안에 문자열
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2


if __name__ == '__main__':
    print(solution('ab6CDE443fgh22iJKlmn1o', '6CD'))
    print(solution('ppprrrogrammers', 'pppp'))