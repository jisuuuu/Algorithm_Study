#로그인 성공?
def solution(id_pw, db):
    answer = 'fail'
    for id, pw in db:
        if id_pw[0] == id:
            if id_pw[1] == pw:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer


def solution2(id_pw, db):
    if id_pw[0] in [ip[0] for ip in db]:
        idx = [ip[0] for ip in db].index(id_pw[0])
        new = [ip[1] for ip in db]

        if id_pw[1] == new[idx]:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail'


if __name__ == '__main__':
    print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
    print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
    print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))