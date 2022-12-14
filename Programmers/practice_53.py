# OX 퀴즈
def solution(quiz):
    answer = []

    for q in quiz:
        q = q.split(' ')
        x = int(q[0])
        y = int(q[2])

        if q[1] == '-':
            answer.append('O' if x - y == int(q[4]) else 'X')
        else:
            answer.append('O' if x + y == int(q[4]) else 'X')

    return answer


if __name__ == '__main__':
    print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
    print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))