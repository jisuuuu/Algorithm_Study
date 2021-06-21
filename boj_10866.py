#덱
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
d = deque()

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if 'push_back' in s:
        num = s.split(' ')[1]
        d.append(num)
    elif 'push_front' in s:
        num = s.split(' ')[1]
        d.appendleft(num)
    elif s == 'pop_front':
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
    elif s == 'pop_back':
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    elif s == 'size':
        print(len(d))
    elif s == 'empty':
        if len(d) != 0:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    elif s == 'back':
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)