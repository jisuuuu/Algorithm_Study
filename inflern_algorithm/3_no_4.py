# 두 리스트 합치기
import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
n = int(input())
n_arr = deque(map(int, input().split()))
m = int(input())
m_arr = deque(map(int, input().split()))
i, j = 0, 0
while True:
    if not n_arr:
        break
    if not m_arr:
        break

    if n_arr[0] < m_arr[0]:
        print(n_arr.popleft(), end=' ')
    else:
        print(m_arr.popleft(), end=' ')

if n_arr:
    print(' '.join(list(map(str, n_arr))))
if m_arr:
    print(' '.join(list(map(str, m_arr))))