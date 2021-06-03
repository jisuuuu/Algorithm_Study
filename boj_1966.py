#프린터 큐
import sys
from collections import deque


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    queue = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    idx = deque(list(range(n)))

    cnt = 0
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()

            if idx.popleft() == m:
                print(cnt)
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())