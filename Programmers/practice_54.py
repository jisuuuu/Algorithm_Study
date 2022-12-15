# A로 B만들기
def solution(before, after):
    return 1 if sorted(list(before)) == sorted(list(after)) else 0


if __name__ == '__main__':
    print(solution('olleh', 'hello'))
    print(solution('allpe', 'apple'))