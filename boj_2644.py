#촌수계산
import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
tree = dict()
for i in range(n):
    tree[i + 1] = set()

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    tree[x].add(y)
    tree[y].add(x)


def bfs(x, y, tree):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    cnt = 0

    while queue:
        cnt += 1
        for _ in range(len(queue)):
            q = queue.popleft()
            if q == y:
                return cnt - 1

            for t in tree[q]:
                if visited[t] == 0:
                    queue.append(t)
                    visited[t] = 1

    return -1


print(tree)
visited = [0 for _ in range(n + 1)]
print(bfs(a, b, tree))