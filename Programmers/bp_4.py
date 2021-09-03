#카펫
import math


def solution(brown, yellow):
    num = brown + yellow
    new = []

    for i in range(num, int(math.sqrt(num)) - 1, -1):
        if num % i == 0:
            new.append([i, num // i])

    for n in new:
        if n[1] == 1:
            continue

        if (n[0] - 2) * (n[1] - 2) == yellow:
            return n