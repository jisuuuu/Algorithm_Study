#배열 원소의 길이
def solution(strlist):
    answer = []

    for s in strlist:
        answer.append(len(s))

    return answer


if __name__ == '__main__':
    print(solution(["We", "are", "the", "world!"]))
    print(solution(["I", "Love", "Programmers."]))