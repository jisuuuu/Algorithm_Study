#모음 제거
def solution(my_string):
    arr = ['a', 'e', 'i', 'o', 'u']

    for a in arr:
        my_string = my_string.replace(a, '')
    return my_string


if __name__ == '__main__':
    print(solution('bus'))
    print(solution('nice to meet you'))