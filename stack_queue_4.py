#다시 풀기
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_weight = []

    queue = deque(truck_weights)

    while queue:
        tmp = queue.popleft()
        now_weight.append(tmp)

        if queue:
            while sum(now_weight) + queue[0] <= weight:
                tmp = queue.popleft()
                now_weight.append(tmp)

                if not queue:
                    break

        while now_weight:
            tmp = now_weight.pop(0)

            if len(now_weight) == 0:
                answer += bridge_length
            else:
                answer += 1

    return answer + 1