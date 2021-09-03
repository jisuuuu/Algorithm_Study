# 2021 KAKAO BLIND RECRUITMENT 순위검색
# 존나어렵당...............!
from itertools import combinations


def solution(info, query):
    answer = []
    db = {}

    for i in info: # info를 정리
        temp = i.split()
        conditions = temp[:-1] #조건을 / 로 16개 경우로 저장
        score = int(temp[-1]) # 값

        for n in range(5): # 조합 중 에 선택되는 것의 갯수가 (0, 1, 2, 3, 4)니까
            combi = list(combinations(range(4), n))
            for c in combi:
                keys = conditions.copy()

                for v in c:
                    keys[v] = '-'
                real_key = '/'.join(keys) # - 포함해서 /을 기준으로 16개씩 만듬듬

                if real_key in db:
                    db[real_key].append(score)
                else:
                    db[real_key] = [score]

    for value in db.values():
        value.sort()

    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cmd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])

        if qry_cmd in db:
            data = db[qry_cmd]
            if len(data) > 0:
                start, end = 0, len(data)

                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1

                answer.append(len(data) - start)
        else:
            answer.append(0)

    return answer


def solution2(info, query):
    answer = []
    info = sorted([i.split() for i in info], key=lambda x:x[4])
    query = [q.replace('and', '').split() for q in query]

    for idx, q in enumerate(query):
        cnt = 0
        for i in info:
            if int(i[4]) >= int(q[4]):
                if (i[0] == q[0] or q[0] == '-') and (i[1] == q[1] or q[1] == '-') and (i[2] == q[2] or q[2] == '-') and (i[3] == q[3] or q[3] == '-'):
                    cnt += 1
            else:
                continue
        answer.append(cnt)
    return answer


if __name__ == '__main__':
    print(solution(["java backend junior pizza 150"
                        , "python frontend senior chicken 210"
                        , "python frontend senior chicken 150"
                        , "cpp backend senior pizza 260"
                        , "java backend junior chicken 80"
                        , "python backend senior chicken 50"],
                    ["java and backend and junior and pizza 100"
                        , "python and frontend and senior and chicken 200"
                        , "cpp and - and senior and pizza 250"
                        , "- and backend and senior and - 150"
                        , "- and - and - and chicken 100"
                        , "- and - and - and - 150"]))
    print(solution2(["java backend junior pizza 150"
                 ,"python frontend senior chicken 210"
                 ,"python frontend senior chicken 150"
                 ,"cpp backend senior pizza 260"
                 ,"java backend junior chicken 80"
                 ,"python backend senior chicken 50"],
             ["java and backend and junior and pizza 100"
                 ,"python and frontend and senior and chicken 200"
                 ,"cpp and - and senior and pizza 250"
                 ,"- and backend and senior and - 150"
                 ,"- and - and - and chicken 100"
                 ,"- and - and - and - 150"]))