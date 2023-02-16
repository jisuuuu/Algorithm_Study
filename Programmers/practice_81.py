#숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    print(s)
    return sum(int(i) for i in s.split())


if __name__ == '__main__':
    print(solution('aAb1B2cC34oOp'))
    print(solution('1a2b3c4d123Z'))