#암호 해독
def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer


if __name__ == '__main__':
    print(solution('dfjardstddetckdaccccdegk', 4))
    print(solution('pfqallllabwaoclk', 2))