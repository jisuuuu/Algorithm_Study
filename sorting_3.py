#H-Index
def solution(citations):
    citations.sort()

    answer = 0

    for i in range(0, len(citations)):
        h = sum(c >= i for c in citations) # i번 이상 인용된 논문 갯수
        k = sum(c <= i for c in citations) # i번 이하 인용된 논문 갯수

        if h >= i and k <= i: # h가 i이상이고 k가 i이하 조건을 만족시키는 값 구하는 과정
            if answer < i: # 가장 큰 수 고르는 과정
                answer = i

    if len(citations) <= citations[0]:
        answer = len(citations)

    return answer