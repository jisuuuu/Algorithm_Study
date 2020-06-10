#정수 내림차순으로 배치하기
def solution(n):
    new = list(str(n))
    new.sort(reverse=True)
    return int("".join(new))