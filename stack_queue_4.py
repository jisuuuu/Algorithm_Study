#다리를 지나는 트럭
from collections import deque


#Test case 5 시간초과 뜸....
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights_deque = deque(truck_weights)
    trucks_on_bridge_deque = deque([0] * bridge_length, maxlen=bridge_length)
    trucks_on_bridge_deque[-1] = truck_weights_deque.popleft()

    while truck_weights_deque:
        if sum(trucks_on_bridge_deque) - trucks_on_bridge_deque[0] + truck_weights_deque[0] > weight:
            trucks_on_bridge_deque.append(0)
            answer += 1
        else:
            trucks_on_bridge_deque.append(truck_weights_deque.popleft())
            answer += 1
    answer += bridge_length

    return answer + 1


#다른 분 코드 여기도 sum, pop 쓰는데 왜징..
def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = []
    on_time = []

    while (truck_weights or on_bridge):
        time += 1
        if (on_time):
            if (on_time[0] + bridge_length == time):
                on_bridge.pop(0)
                on_time.pop(0)
        if (truck_weights):
            if (sum(on_bridge) + truck_weights[0] <= weight):
                on_bridge.append(truck_weights.pop(0))
                on_time.append(time)

    return time