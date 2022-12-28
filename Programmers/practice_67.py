# 컨트롤 제트
def solution(s):
    answer, remember_num = 0, 0
    new = s.split(' ')

    for n in new:
        if n != 'Z':
            answer += int(n)
            remember_num = int(n)
        else:
            answer -= remember_num

    return answer


if __name__ == '__main__':
    print(solution("1 2 Z 3"))
    print(solution("10 20 30 40"))
    print(solution("10 Z 20 Z 1"))
    print(solution("10 Z 20 Z"))
    print(solution("-1 -2 -3 Z"))