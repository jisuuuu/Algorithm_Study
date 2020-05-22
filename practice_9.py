#수박수박수박수박수박수?
from itertools import cycle


def solution(n):
    pattern = ['수', '박']
    answer = ''

    for i, p in zip([i for i in range(n)], cycle(pattern)):
        answer += p
    return answer