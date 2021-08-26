# 두 리스트 합치기
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
n_arr = deque(a)
m = int(input())
b = list(map(int, input().split()))
m_arr = deque(b)

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

p1 = p2 = 0
c = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m :
    c = c + b[p2:]
print(c)