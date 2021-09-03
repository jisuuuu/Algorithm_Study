#실패율
def solution(N, stages):
    answer = dict()

    for i in range(1, N + 1):

        total = 0
        i_total = 0
        for s in stages:
            if i <= s:
                total += 1
            if i == s:
                i_total += 1

        if total != 0:
            answer[i] = i_total / total
        else:
            answer[i] = 0

    answer = sorted(answer.items(), key=lambda item: item[1], reverse=True)

    return [a[0] for a in answer]