#최댓값과 최솟값
def solution(s):
    new = list(map(int, s.split(' ')))

    answer = ""
    answer += str(min(new))
    answer += " "
    answer += str(max(new))
    return answer