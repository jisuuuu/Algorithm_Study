#2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = set(report)
    user = defaultdict(set)
    count = defaultdict(int)

    for r in report:
        _from, _to = r.split()
        user[_from].add(_to)
        count[_to] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if count[u] >= k:
                result += 1
        answer.append(result)

    return answer