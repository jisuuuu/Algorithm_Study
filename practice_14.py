#124 나라의 숫자
def solution(n):
    answer = ''
    remainder = -1

    while n != 0:
        remainder = n % 3
        n = n // 3

        if remainder == 0:# 나누어떨어지는 것 한 번더 체크해야하기 때문에 n -= 1
            answer = "4" + answer
            n -= 1

        elif remainder == 1:
            answer = "1" + answer

        else:
            answer = "2" + answer

    return answer