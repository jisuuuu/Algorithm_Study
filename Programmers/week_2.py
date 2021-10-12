# 위클리 챌린지 - 최소직사각형
def solution(sizes):
    answer = 0
    long = []
    short = []

    for s in sizes:
        if s[0] > s[1]:
            long.append(s[0])
            short.append(s[1])
        else:
            short.append(s[0])
            long.append(s[1])

    answer = max(short) * max(long)
    return answer