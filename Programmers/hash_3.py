#위장
def solution(clothes):
    answer = dict()

    for clothe in clothes:
        if clothe[1] in answer:
            answer[clothe[1]] += 1
        else:
            answer[clothe[1]] = 1

    cnt = 1

    for i in answer.values():
        cnt *= (i + 1) #안 입고 있는 경우 있으니 +1

    return cnt - 1 # 아예 벗고 있는 경우는 없으니까 -1


def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer