#월간 코드 챌린지 시즌2 음양 더하기
def solution(absolutes, signs):
    answer = 0

    for i, a in enumerate(absolutes):
        if signs[i]:
            answer += a
        else:
            answer -= a

    return answer