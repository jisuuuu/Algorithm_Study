#한 번만 등장한 문자
def solution(s):
    answer = dict()

    for k in sorted(s):
        if k not in answer.keys():
            answer[k] = 1
        else:
            answer[k] += 1
    answer = {k: v for k, v in answer.items() if v == 1}

    return ''.join(answer.keys())


if __name__ == '__main__':
    print(solution('abcabcadc'))
    print(solution('abdc'))
    print(solution('hello'))