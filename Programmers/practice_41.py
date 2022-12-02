#문자열 정렬하기 (2)
def solution(my_string):
    new = [l.lower() for l in list(my_string)]
    return ''.join(sorted(new))


if __name__ == '__main__':
    print(solution("Bcad"))
    print(solution("heLLo"))
    print(solution("Python"))