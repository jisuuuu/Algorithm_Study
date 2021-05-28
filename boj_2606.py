#바이러스
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = dict()

for i in range(n):
    graph[i + 1] = set()

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].add(j)
    graph[j].add(i)


def bfs(x, graph):
    queue = [x]

    while queue:
        for q in graph[queue.pop()]:
            if q not in visited:
                visited.append(q)
                queue.append(q)


visited = []
bfs(1, graph)
print(len(visited) - 1)