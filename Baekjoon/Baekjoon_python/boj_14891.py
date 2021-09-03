# 톱니바퀴
import sys, collections

s = []
for _ in range(4):
    s.append(collections.deque(list(input())))

K = int(sys.stdin.readline())
R = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]


# 왼쪽 톱니바퀴 확인
def left(num, direction):
    if num < 0:
        return
    if s[num][2] != s[num + 1][6]:
        left(num - 1, -direction)
        s[num].rotate(direction)


# 오른쪽 톱니바퀴 확인
def right(num, direction):
    if num > 3:
        return
    if s[num][6] != s[num - 1][2]:
        right(num + 1, -direction)
        s[num].rotate(direction)


for i in range(K):
    num = R[i][0] - 1
    direction = R[i][1]

    left(num - 1, -direction)
    right(num + 1, -direction)
    s[num].rotate(direction)

res = 0

for i in range(4):
    if s[i][0] == '1':
        res += (2 ** i)
print(res)
