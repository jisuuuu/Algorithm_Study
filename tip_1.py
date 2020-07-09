#짝지어 제거하기
from collections import deque


def solution(s):
    stack = []
    s = deque(list(s))
    stack.append(s.popleft())

    while s:
        if len(stack) == 0:
            stack.append(s.popleft())

        elif stack[-1] == s[0]:
            stack.pop()
            s.popleft()

        else:
            stack.append(s.popleft())

    if len(stack) == 0:
        return 1
    else:
        return 0