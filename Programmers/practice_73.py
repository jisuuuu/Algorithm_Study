#중복된 문자 제거
def solution(my_string):
    answer = ''.join(list(dict.fromkeys(my_string)))
    return answer


if __name__ == '__main__':
    print(solution('people'))
    print(solution('We are the world'))