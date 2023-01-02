#인덱스 바꾸기
def solution(my_string, num1, num2):
    return my_string[:num1] + my_string[num2] + my_string[num1 + 1:num2] + my_string[num1] + my_string[num2 + 1:]


if __name__ == '__main__':
    print(solution('hello', 1, 2))
    print(solution('I love you', 3, 6))