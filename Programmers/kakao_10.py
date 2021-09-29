#2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
def solution(s):
    answer = 0
    result = ''
    num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4
        , 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    stack = []

    for ss in s:
        if ss.isdigit():
            if stack:
                result += str(num[''.join(stack)])
                stack = []
            result += ss
        else:
            stack.append(ss)

    if stack:
        k = 3
        while True:
            if ''.join(stack[:k]) in num.keys():
                result += str(num[''.join(stack[:k])])
                result += str(num[''.join(stack[k:])])
                break

            k += 1

    return int(result)
# 런타임 에러 -> stack으로 만들어서 넝어서 그런듯 그냥 문자열이니까 상관없이해도 됨

def solution(s):
    answer = 0
    result = ''
    num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4
        , 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    result = ''
    english = ''

    for ss in s:
        if ss.isdigit():
            result += ss
        elif ss.isalpha():
            english += ss
            if english in num.keys():
                result += str(num[english])
                english = ''

    return int(result)

def solution(s):
    english = ['zero', 'one', 'two', 'three', 'four'
        , 'five', 'six', 'seven', 'eight', 'nine']

    answer = ''

    for idx, num in enumerate(english):
        if num in s:
            s = s.replace(num, str(idx))
        answer = s

    return int(answer)