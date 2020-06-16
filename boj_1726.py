#로봇
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
c = []


def bfs(robot, matrix, des_x, des_y, des_p):
    q.append(robot)
    c.append(robot)

    cnt = 0
    while q:
        qlen = len(q)
        while qlen:
            x = q.popleft()

            if x == [des_x, des_y, des_p]:
                return cnt


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().rstrip().split())
    matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
    start_x, start_y, start_p = map(int, sys.stdin.readline().rstrip().split())
    des_x, des_y, des_p = map(int, sys.stdin.readline().rstrip().split())

    robot = [start_x, start_y, start_p]

    bfs(robot, matrix, des_x, des_y, des_p)