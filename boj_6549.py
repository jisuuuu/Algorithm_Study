#히스토그램에서 가장 큰 직사각형
import sys
from collections import deque
while True:
    arr = list(map(int, sys.stdin.readline().split(' ')))
    n = arr.pop(0)
    if n == 0:
        break

    answer = 0
    stack = deque()

    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1

            answer = max(answer, width * arr[tmp])
        stack.append(i)

    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1

        answer = max(answer, width * arr[tmp])

    print(answer)