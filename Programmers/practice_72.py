# 다항식 더하기
def solution(polynomial):
    answer = ''
    new_polynomial = sorted(polynomial.replace(' ', '').split('+'))

    x_num = 0
    num = 0
    for n in new_polynomial:
        if 'x' in n:
            if n.replace('x', '') != '':
                x_num += int(n.replace('x', ''))
            else:
                x_num += 1
        else:
            num += int(n)

    if x_num != 0 and num != 0:
        if x_num == 1:
            answer += 'x' + ' + ' + str(num)
        else:
            answer += str(x_num) + 'x' + ' + ' + str(num)
    elif x_num == 0 and num != 0:
        answer += str(num)
    elif x_num != 0 and num == 0:
        if x_num == 1:
            answer += 'x'
        else:
            answer += str(x_num) + 'x'

    return answer


if __name__ == '__main__':
    print(solution("3x + 7 + x"))
    print(solution("x + x + x"))
    print(solution("5x + 16 + x + 12"))