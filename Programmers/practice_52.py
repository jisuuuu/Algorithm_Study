#대문자와 소문자
def solution(my_string):
    answer = ''

    for s in my_string:
        if s.isupper():
            answer += s.lower()
        else:
            answer += s.upper()

    return answer


if __name__ == '__main__':
    print(solution('cccCCC'))
    print(solution('abCdEfghIJ'))