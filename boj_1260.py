#DFS와 BFS
import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dfs_res = ''
bfs_res = ''

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[x][y] = matrix[y][x] = 1


def dfs(start_node):
    global dfs_res

    visited[start_node] = 1
    dfs_res += str(start_node) + ' '

    for i in range(1, n + 1):
        if visited[i] == 0 and matrix[start_node][i] == 1:
            dfs(i)


def bfs(start_node):
    global bfs_res

    queue = [start_node]
    visited[start_node] = 1

    while queue:
        start_node = queue.pop(0)
        bfs_res += str(start_node) + ' '

        for i in range(1, n + 1):
            if visited[i] == 0 and matrix[start_node][i] == 1:
                queue.append(i)
                visited[i] = 1


visited = [0 for _ in range(n + 1)]
dfs(v)
print(dfs_res)
visited = [0 for _ in range(n + 1)]
bfs(v)
print(bfs_res)