#이진 변환 반복하기
def solution(s):
    answer = []
    zero = 0
    k = 0

    while s != '1':
        k += 1
        zero += s.count('0')
        s = format(s.count('1'), 'b')
        answer = [k, zero]

    return answer