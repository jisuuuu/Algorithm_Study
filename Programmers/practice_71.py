#외계어 사전
def solution(spell, dic):
    answer = 2
    for d in dic:
        cnt = 0
        for s in spell:
            if s in d:
                cnt += 1

        if cnt == len(spell):
            answer -= 1
            break

    return answer


if __name__ == '__main__':
    print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
    print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
    print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))