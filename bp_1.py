#모의고사
from itertools import cycle


def solution(answers):
    answer = []
    scores = [0, 0, 0]

    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for p1, p2, p3, a in zip(cycle(pattern1), cycle(pattern2), cycle(pattern3), answers):
        if p1 == a:
            scores[0] += 1
        if p2 == a:
            scores[1] += 1
        if p3 == a:
            scores[2] += 1

    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)

    return answer