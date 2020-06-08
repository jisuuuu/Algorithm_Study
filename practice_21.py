#N개의 최소공배수
import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


def solution(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))

    return arr[0]