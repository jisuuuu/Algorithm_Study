#라면공장
import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    h = []

    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(h, -supplies[i]) # -1 처리 하는 이유: heapq 라이브러리 최소 힙 기반
            idx = i + 1

        stock += (heapq.heappop(h) * -1) #꺼낼 때도 -1 곱해서 원래 수로 만들어서 사용
        answer += 1

    return answer