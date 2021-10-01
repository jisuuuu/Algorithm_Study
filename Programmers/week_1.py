#위클리 챌린지 - 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0

    for i in range(1, count + 1):
        answer += price * i

    if answer - money < 0:
        return 0

    return answer - money