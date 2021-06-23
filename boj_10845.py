#큐
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if 'push' in s:
        num = s.split(' ')[1]
        queue.append(num)
    elif s == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif s == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)