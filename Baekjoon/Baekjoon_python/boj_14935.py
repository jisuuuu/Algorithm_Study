#FA
import sys


def solution(n):
    s = str(n)

    if n == int(s[0]) * len(s):
        return 'FA'
    return solution(int(s[0]) * len(s))


x = int(sys.stdin.readline().rstrip())
print(solution(x))