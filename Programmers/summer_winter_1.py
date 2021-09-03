#스킬트리
def solution(skill, skill_trees):
    answer = 0

    for i, st in enumerate(skill_trees):
        idx = 0
        for s in st:
            if s in skill:
                if skill[idx] == s:
                    idx += 1
                else:
                    break
        else:
            answer += 1

    return answer