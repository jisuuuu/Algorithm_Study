#자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    new = str(n)
    for i in range(len(new) - 1, -1, -1):
        answer.append(int(new[i]))
    return answer