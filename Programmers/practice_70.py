#문자열 정렬하기 (1)
def solution(my_string):
    answer = [int(s) for s in my_string if s.isdigit()]
    return sorted(answer)


if __name__ == '__main__':
    print(solution('hi12392'))
    print(solution('p2o4i8gj2'))
    print(solution('abcde0'))