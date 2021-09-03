#소수찾기
import itertools


def solution(numbers):
    answer = 0
    new = []

    for i in range(1, len(numbers) + 1):
        perm = itertools.permutations(list(numbers), i)
        for i in list(perm):
            num = int("".join(list(i)))
            new.append(num)

    new = set(new)

    for n in new:
        if n < 2:
            continue
        elif n == 2:
            answer += 1
        else:
            for i in range(2, n):
                if n % i == 0:
                    break
                elif i == n - 1:
                    answer += 1

    return answer