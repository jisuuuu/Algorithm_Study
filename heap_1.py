#더 맵게

#효율성 다 틀림
def solution(scoville, K):
    answer = 0

    while scoville[0] < K:
        scoville.sort()
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        answer += 1
        num1 = scoville.pop(0)
        num2 = scoville.pop(0)

        new = num1 + (num2 * 2)

        scoville.append(new)

    return answer


#heapq 이분탐색 유용한 라이브러리, 자동으로 정렬해줌
import heapq


def solution1(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        if len(heap) == 1 and heap[0] < K:
            return -1
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)

        new = num1 + (num2 * 2)

        heapq.heappush(heap, new)

        answer += 1

    return answer