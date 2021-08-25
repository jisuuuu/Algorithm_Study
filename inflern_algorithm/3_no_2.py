#숫자만 추출
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
word = input()
queue = deque()
res = 0
for w in word:
    if w.isdecimal():
        res = res * 10 + int(w)
    if w.isdigit():
        if w == '0' and not queue:
            continue
        queue.appendleft(w)
print(res)
n = 0

for i, q in enumerate(queue):
    n += (10 ** i) * int(q)
print(n)

cnt = 0
for i in range(1, int(n ** (0.5)) + 1):
    if n % i == 0:
        cnt += 1
        if i != (n // i):
            cnt += 1
print(cnt)