#기능개발
import math

def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

    cnt = 1

    while progresses:
        tmp = progresses.pop(0)

        if len(progresses) == 0:
            answer.append(cnt)
            break

        else:
            while progresses and tmp >= progresses[0]:
                progresses.pop(0)
                cnt += 1

        answer.append(cnt)
        cnt = 1

    return answer

def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    front = 0

    for idx in range(len(progresses)):
        if progresses[front] < progresses[idx]:
            answer.append(idx - front)
            front = idx
    answer.append(len(progresses) - front)

    return answer